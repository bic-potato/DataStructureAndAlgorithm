cmake_minimum_required(VERSION 3.17)
project(small C)

set(CMAKE_C_STANDARD 11)

add_library(small SHARED library.c library.h)