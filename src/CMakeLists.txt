cmake_minimum_required(VERSION 2.8)
project(MyHello CXX)

add_definitions("-std=c++11")

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_library(hello hello.cpp)
add_executable(greet main.cpp)

target_link_libraries(greet hello ${CONAN_LIBS})
