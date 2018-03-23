load("@my_deps//:requirements.bzl", "requirement")

py_binary(
    name = "main",
    srcs = ["main.py"],
    main = "main.py",
    deps = [
        # This takes the name as specified in requirements.txt
        requirement("requests"),
    ],
)
