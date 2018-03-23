import requests

def print_lib_version():
  return requests.__version__

if __name__ == "__main__":
  print print_lib_version()
