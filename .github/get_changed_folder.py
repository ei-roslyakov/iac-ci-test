import argparse
import ast


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--folders", nargs="+", default=[]),

    return parser.parse_args()


def get_project_root(path_string, sep="/"):
    parts = path_string.split(sep)

    if "dev" in parts:
        index = parts.index("dev")
        return sep.join(parts[: index + 1])

    if "prod" in parts:
        index = parts.index("prod")
        return sep.join(parts[: index + 1])


def main():
    args = parse_args()

    folders = args.folders[0]

    folder_list = []

    for item in ast.literal_eval(folders):
        folder_path = get_project_root(item)
        if folder_path is not None and folder_path not in folder_list:
            folder_list.append(folder_path)

    print(folder_list)


if __name__ == "__main__":
    main()
