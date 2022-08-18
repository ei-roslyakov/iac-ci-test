import argparse
from traceback import print_tb
import requests
import loguru

logger = loguru.logger


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-t",
        "--token",
        required=True,
        type=str,
        action="store",
        help="GH token",
    ),
    parser.add_argument(
        "-o",
        "--owner",
        required=False,
        default="ei-roslyakov",
        type=str,
        action="store",
        help="GH repo owner",
    ),
    parser.add_argument(
        "-r",
        "--repo",
        required=False,
        default="iac-ci-test",
        type=str,
        action="store",
        help="GH repo name",
    ),
    parser.add_argument(
        "-p",
        "--pr",
        required=True,
        type=str,
        action="store",
        help="GH token",
    ),
    parser.add_argument(
        "--get-reviewers",
        required=False,
        type=bool,
        default=False,
        action=argparse.BooleanOptionalAction,
        help="Get list of PR reviewers",
    )

    return parser.parse_args()


def get_reviewers(token: str, pr_number: str, owner: str, repo: str):
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"token {token}",
    }
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/reviews"
    reviewers_list = []
    try:
        reviewers_r = requests.get(url, headers=headers)
        logger.info(f"Get reviewers status: {reviewers_r.status_code}")
        reviewers = reviewers_r.json()
        for user in reviewers:
            if user["user"]["login"] not in reviewers_list:
                reviewers_list.append(user["user"]["login"])

    except requests.exceptions.RequestException as e:
        logger.exception(f"Somthing went wrong {e}")

    logger.info(f"Reviewers are: {reviewers_list}")
    return reviewers_list

def delete_reviewers(
    token: str, pr_number: str, reviewers: list, owner: str, repo: str
):
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"token {token}",
    }
    data = {"reviewers": reviewers}
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/requested_reviewers"

    try:
        reviewers_r = requests.delete(url, headers=headers, json=data)
        logger.info(f"Delete reviewers status: {reviewers_r.status_code}")
        logger.info(f"Reviewers are deleted: {reviewers}")
        return reviewers_r.status_code
    except requests.exceptions.RequestException as e:
        logger.exception(f"Somthing went wrong {e}")


def set_reviewers(token: str, pr_number: str, reviewers: list, owner: str, repo: str):
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"token {token}",
    }
    data = {"reviewers": reviewers}
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/requested_reviewers"

    try:
        reviewers_r = requests.post(url, headers=headers, json=data)
        logger.info(f"Setreviewers status: {reviewers_r.status_code}")
        logger.info(f"Reviewers are attached: {reviewers}")
        return reviewers_r.status_code
    except requests.exceptions.RequestException as e:
        logger.exception(f"Somthing went wrong {e}")


def main():

    args = parse_args()

    logger.info(f"Application started")
    if args.get_reviewers:
        reviewers = get_reviewers(args.token, args.pr, args.owner, args.repo)
        print(reviewers)
    
    if not args.get_reviewers:
        reviewers = get_reviewers(args.token, args.pr, args.owner, args.repo)
        removed_reviewers = delete_reviewers(
            args.token, args.pr, reviewers, args.owner, args.repo
        )
        attached_removed_reviewers = set_reviewers(
            args.token, args.pr, reviewers, args.owner, args.repo
        )
    logger.info(f"Application finished")


if __name__ == "__main__":
    main()
