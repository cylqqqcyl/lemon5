import os


# Reference: https://github.com/coqui-ai/TTS/blob/dev/tests/__init__.py

def get_tests_path():
    """Return thte path to the test directory.
    """

    return os.path.dirname(os.path.realpath(__file__))

def get_tests_input_path():
    """Returns the path to the test data directory.
    """

    return os.path.join(get_tests_path(), "inputs")

def get_tests_data_path():
    """Return the path to the test data directory.
    """

    return os.path.join(get_tests_data_path(), "data")

def get_tests_output_path():
    """Returns the path to the directory for test outputs.
    """

    path = os.path.join(get_tests_path(), "outputs")
    os.makedirs(path, exist_ok=True)
    return path

def run_cli(command):
    """Run command.
    """

    exit_status = os.system(command)
    assert exit_status == 0, f" [!] command `{command}` failed."

