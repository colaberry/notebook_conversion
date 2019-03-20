# notebook_conversion

A standalone python application for benchmarking conversion of `*.ipynb` to `.html` file.

**Proposed Solution**

- Create a python file that pulls all the `*.ipynb` from a file and converts it into `.html` 
- Create decorators on each functions to measure time for ~150 files.
- Can also create a bash file that facilitates the same thing periodically on the server.


**Styling Guidelines**

- Please name your variables, classes, methods adhering to [PEP8 Guidelines](https://www.python.org/dev/peps/pep-0008/)
- tl;dr variables should be underscore separated, class name should be CamelCase and functions / methods should be underscore_separated.
- Refrain from using `global`
- Code should not exceed 80 characters.
- Please do not push `.pyc` files or any dunder files (like \__pycache\__)
