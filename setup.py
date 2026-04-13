from setuptools import setup
from Cython.Build import cythonize

setup(
    name="DivergentPathStripper",
    ext_modules=cythonize("reacher.py", compiler_directives={'language_level' : "3"}),
    zip_safe=False,
)
