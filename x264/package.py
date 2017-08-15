name = "x264"
version = "head"
authors = [""]
description = """ """
requires = []
build_requires = []

variants = [
    ["platform-linux", "arch-x86_64"]
]

tools = [
    "x264"
]

uuid = "repository.x264"

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
        env.OPENEXR_INCLUDE_DIR = "{root}/include"
