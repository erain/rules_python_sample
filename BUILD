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

py_test(
    name = "main_test",
    srcs = ["main_test.py"],
    deps = [
        ":main",
    ],
)
