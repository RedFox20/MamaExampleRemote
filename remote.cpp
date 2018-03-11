#include "remote.h"
#include <cstdio>

namespace example
{
    void print_remote(const std::string& str)
    {
        printf("ExampleRemote says: %s\n", str.c_str());
    }
}
