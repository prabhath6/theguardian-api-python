from unittest import main


def load_tests(loader, standard_tests, pattern):

    """
    :param loader:
    :param standard_tests:
    :param pattern:
    :return:
    """

    package_tests = loader.discover(start_dir="tests", pattern="test_*.py")
    standard_tests.addTests(package_tests)

    return standard_tests

if __name__ == '__main__':
    main()
