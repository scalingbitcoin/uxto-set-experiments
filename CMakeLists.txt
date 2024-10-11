cmake_minimum_required(VERSION 3.15)
project(uxto-set-experiments CXX)
set(CMAKE_CXX_STANDARD 20)


find_package(node REQUIRED)
find_package(fmt REQUIRED)
find_package(absl REQUIRED)
find_package(Boost REQUIRED)
# find_package(robin-hood-hashing REQUIRED)
# find_package(robin_hood_hashing REQUIRED)
find_package(unordered_dense REQUIRED)
find_package(svector REQUIRED)

# Link against jemalloc
# Fedora: sudo dnf install jemalloc-devel
# RaspiOS: sudo apt install libjemalloc-dev
# set(COMMON_DEFS JEMALLOC)
# find_library(JEMALLOC_LIB jemalloc)
# if(NOT JEMALLOC_LIB)
#   message(FATAL_ERROR "Could not find jemalloc.")
# else()
#   message("-- Found jemalloc: ${JEMALLOC_LIB}")
# endif()

find_package(PkgConfig REQUIRED)
pkg_check_modules(JEMALLOC jemalloc)

message("-- Found jemalloc: JEMALLOC_INCLUDE_DIRS: ${JEMALLOC_INCLUDE_DIRS}")
message("-- Found jemalloc: JEMALLOC_LIBRARY_DIRS: ${JEMALLOC_LIBRARY_DIRS}")
message("-- Found jemalloc: JEMALLOC_CFLAGS_OTHER: ${JEMALLOC_CFLAGS_OTHER}")

include_directories(${JEMALLOC_INCLUDE_DIRS})
link_directories(${JEMALLOC_LIBRARY_DIRS})
add_definitions(${JEMALLOC_CFLAGS_OTHER})



add_definitions(-DKTH_CURRENCY_BCH)
add_definitions(-DJEMALLOC)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -march=native")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -march=native")


include_directories(${PROJECT_SOURCE_DIR}/include)
# ---------------------------------------------------------------

add_executable(${PROJECT_NAME} src/main.cpp)

target_link_libraries(${PROJECT_NAME} PUBLIC node::node)
target_link_libraries(${PROJECT_NAME} PUBLIC fmt::fmt-header-only)
# target_link_libraries(${PROJECT_NAME} PUBLIC ${JEMALLOC_LIB})
target_link_libraries(${PROJECT_NAME} PUBLIC ${JEMALLOC_LIBRARIES})


install(TARGETS ${PROJECT_NAME} DESTINATION "."
        RUNTIME DESTINATION bin
        ARCHIVE DESTINATION lib
        LIBRARY DESTINATION lib
        )
