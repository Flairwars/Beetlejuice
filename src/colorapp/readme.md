compile and wrap with tbenthompson/cppimport and pybind11, which creates an importable python library

**TODO** pybind11 included as git submodule in <rootdir>/src/colorapp/pybind11

**TODO** add `pip install cppimport` somewhere relevant

**NOTE: code cannot be compiled yet**
## In python code
```python
import cppimport.import_hook
import colorapp.cpp
```
Then call ``output=colorapp.recolor(params)``. Imported c++ code will compile on launch and.

#### Expected inputs:
1. flattened list of pixel value tuples in an RGBA order and format, created using `list(Image.getdata())`
2. image height
3. image width
4. target RGB list
5. intensity

#### Expected output:
Array object to be read by `Image.fromarray`
