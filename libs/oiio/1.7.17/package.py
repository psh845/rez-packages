# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building, scope  # make linter happy


name = "oiio"

version = "1.7.17"

authors = [
    "Larry Gritz"
]

description = \
    """
    OpenImageIO is a library for reading and writing images, and a bunch of related classes, utilities, and applications.
    """

requires = [
    "ocio-1.0.9",
    # "ilmbase-2",
    "openexr-2",
    "jpeg-1",
    "tiff-4",
    "png-1",
    "zlib-1",
    "qt",
    "boost-1",
    "ffmpeg-2.8",
    "python-2.7"
]

variants = [
    ["platform-linux", "arch-x86_64"]
]

tools = [
    "maketx",
    "iv",
    "igrep",
    "iinfo",
    "idiff",
    "iconvert"
    "oiiotool"
]

uuid = "repository.oiio"


def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PYTHONPATH.append("{root}/lib/python2.7/site-packages")

    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
