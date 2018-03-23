http_archive(
    name = "bazel_toolchains",
    sha256 = "699b55a6916c687f4b7dc092dbbf5f64672cde0dc965f79717735ec4e5416556",
    strip_prefix = "bazel-toolchains-44200e0c026d86c53470d107b3697a3e46469c43",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/bazel-toolchains/archive/44200e0c026d86c53470d107b3697a3e46469c43.tar.gz",
        "https://github.com/bazelbuild/bazel-toolchains/archive/44200e0c026d86c53470d107b3697a3e46469c43.tar.gz",
    ],
)

http_archive(
    name = "io_bazel_rules_python",
    sha256 = "0d1810fecc1bf2b6979d2af60e157d93d3004805bd8b7fda6eb52dda13480dca",
    strip_prefix = "rules_python-115e3a0dab4291184fdcb0d4e564a0328364571a",
    urls = [
        "https://github.com/bazelbuild/rules_python/archive/115e3a0dab4291184fdcb0d4e564a0328364571a.tar.gz",
    ],
)

# For PIP support:
load("@io_bazel_rules_python//python:pip.bzl", "pip_repositories", "pip_import")

pip_repositories()

# This rule translates the specified requirements.txt into
# @my_deps//:requirements.bzl, which itself exposes a pip_install method.
pip_import(
    name = "my_deps",
    requirements = "//:requirements.txt",
)

# Load the pip_install symbol for my_deps, and create the dependencies'
# repositories.
load("@my_deps//:requirements.bzl", "pip_install")

pip_install()
