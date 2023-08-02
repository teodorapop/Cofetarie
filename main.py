from Logic.file_ops import load_file
from Tests.run_all import run_all_tests
from UI.console import run_console


def main():

    prajituri = load_file()

    undo_list = []

    run_console(prajituri, undo_list)


run_all_tests()
main()
