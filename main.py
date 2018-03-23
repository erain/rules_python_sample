import requests

def print_lib_version():
    print requests.__version__

if __name__ == "__main__":
    print_lib_version()
