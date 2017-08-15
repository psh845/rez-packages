find_package(PkgConfig)
set( ENV{PKG_CONFIG_PATH} $ENV{PKG_CONFIG_PATH}:$ENV{REZ_OCIO_ROOT}/lib/pkgconfig)
pkg_check_modules(OCIO REQUIRED OpenColorIO)
set(ocio_INCLUDE_DIRS       ${OCIO_INCLUDE_DIRS})
set(ocio_LIBRARY_DIRS       ${OCIO_LIBRARY_DIRS})
set(ocio_LIBRARIES ${OCIO_LIBRARIES})
