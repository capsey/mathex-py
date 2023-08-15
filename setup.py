from setuptools import setup
from Cython.Build import cythonize

setup(
    name="mathex",
    ext_modules=cythonize("src/mathex/*.pyx", language_level="3"),
    packages=["mathex"],
    package_dir={"mathex": "src/mathex"},
)
