import sys


def get_argv():
    argv = sys.argv
    return argv


def load_file(path):
    with open(f"{path}", "r") as file:
        content = file.read()
        return content


init_word = ["int", "str"]
