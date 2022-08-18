import argparse
import requests


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('t', '--token', required=True, type=str, default="default", action="store", help="GH token"),
    parser.add_argument('--get-reviewers',
        required=False,
        type=bool,
        default=False,
        action=argparse.BooleanOptionalAction,
        help="Add"),
    parser.add_argument('--delete-reviewers',required=False,
        type=bool,
        default=False,
        action=argparse.BooleanOptionalAction,
        help="Add"),
    parser.add_argument('--set-reviewers',required=False,
        type=bool,
        default=False,
        action=argparse.BooleanOptionalAction,
        help="Add"),

    return parser.parse_args()


def get_reviewers(token: str, pr_number: str):
    
    try:
        reviewers = requests.get(f"https://api.github.com/repos/ei-roslyakov/iac-ci-test/pulls/{pr_number}/requested_reviewers",
        headers={"Accept: application/vnd.github+json", f"Authorization: token {token}"})

        return reviewers
    except requests.exceptions.HTTPError as e:
        print(f"Somthing went wrong {e}")
        


def main():

    args = parse_args()

    get_reviewers(args.token, "13")


if __name__ == "__main__":
    main()