CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)


rez_find_packages(PREFIX pkgs AUTO)


set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(url https://github.com/AnimalLogic/AL_USDMaya.git)
set(tag ${version})


if(${REZ_BUILD_INSTALL})
    set(install_cmd make ${make_args})
else()
    set(install_cmd "")
endif()

set(CMAKE_ARGS
    -DCMAKE_BUILD_TYPE=RelWithDebInfo
    -DUSD_ROOT=$ENV{REZ_USD_ROOT}
    -DMAYA_LOCATION=$ENV{MAYA_LOCATION}
    #-DOPENEXR_LOCATION=$ENV{REZ_OPENEXR_ROOT}
    #-DGLEW_LOCATION=$ENV{REZ_GLEW_ROOT}
    -DBOOST_ROOT=$ENV{REZ_BOOST_ROOT}
    -DPXR_BUILD_TESTS=OFF
    -DSKIP_USDMAYA_TESTS=ON
)


ExternalProject_add(
    AL_USDMaya
    GIT_REPOSITORY ${url}
    GIT_TAG ${tag}
    PREFIX AL_USDMaya
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} ${CMAKE_ARGS}
    INSTALL_COMMMAND "${install_cmd}"
)

