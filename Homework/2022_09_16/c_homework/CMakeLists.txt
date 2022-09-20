cmake_minimum_required(VERSION 3.23)
project(c_math C)
project(c_age C)
project(c_nacl C)

set(CMAKE_C_STANDARD 11)

add_executable(c_math math_stuff.c)
add_executable(c_age whats_your_age.c)
add_executable(c_nacl na_cl.c)
