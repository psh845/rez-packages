find_package(PkgConfig)
set( ENV{PKG_CONFIG_PATH} $ENV{PKG_CONFIG_PATH}:$ENV{REZ_SHIBOKEN_ROOT}/lib/pkgconfig)
pkg_check_modules (SHIBOKEN REQUIRED shiboken)
set(shiboken_INCLUDE_DIRS   	${SHIBOKEN_INCLUDE_DIRS})
set(shiboken_LIBRARY_DIRS   	${SHIBOKEN_LIBRARY_DIRS})
set(shiboken_LIBRARIES ${SHIBOKEN_LIBRARIES})
