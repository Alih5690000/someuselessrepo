#include <iostream>
#include <vector>
#include <cstdlib>

int main(){
    std::vector<void*> ptrs;
    for (;;){
        ptrs.push_back(malloc(2048));
    }
    return 0;
}