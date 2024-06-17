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

add_definitions(-DKTH_CURRENCY_BCH)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -march=native")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -march=native")


include_directories(${PROJECT_SOURCE_DIR}/include)
# ---------------------------------------------------------------

add_executable(${PROJECT_NAME} src/main.cpp)

target_link_libraries(${PROJECT_NAME} PUBLIC node::node)
target_link_libraries(${PROJECT_NAME} PUBLIC fmt::fmt-header-only)
# target_link_libraries(${PROJECT_NAME} PUBLIC ${JEMALLOC_LIB})

install(TARGETS ${PROJECT_NAME} DESTINATION "."
        RUNTIME DESTINATION bin
        ARCHIVE DESTINATION lib
        LIBRARY DESTINATION lib
        )
