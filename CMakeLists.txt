cmake_minimum_required(VERSION 3.6)
project(example_remote)


file(GLOB_RECURSE EXAMPLE_REMOTE_SOURCES *.cpp *.h)
source_group(ExampleRemote FILES ${EXAMPLE_REMOTE_SOURCES})
add_library(ExampleRemote STATIC ${EXAMPLE_REMOTE_SOURCES})

install(TARGETS ExampleRemote DESTINATION bin)
