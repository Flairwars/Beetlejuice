//cppimport
#include "pybind11/pybind11.h"
#include <list>
#include <tuple>

namespace py = pybind11;


//threaded function that takes and returns std::list<std::tuple<int>>
std::list<std::tuple<int>> recolor_thread(){
    //recolor and manage return
}

PYBIND11_MODULE(recolor, m){

}

<%
setup_pybind11(cfg)
<%