from distutils.core import setup,Extension
from    Cython.Build import cythonize

ext=Extension(name="PrimNumberWithMultiThreading",sources=["PrimNumberWithMultiThreading.pyx"])
setup(ext_modules=cythonize(ext))