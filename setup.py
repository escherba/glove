import os
import numpy as np
from setuptools import setup, find_packages
from Cython.Build import cythonize


os.environ["CFLAGS"]="-I" + np.get_include()


def readfile(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='glove',
    version='1.0.1',
    description='Python package for computing embeddings from co-occurence matrices',
    long_description=readfile('README.md'),
    packages=find_packages(),
    py_modules=[],
    author='Jonathan Raiman',
    author_email='jraiman at mit dot edu',
    url='https://github.com/JonathanRaiman/glove',
    download_url='https://github.com/JonathanRaiman/glove',
    keywords='NLP, Machine Learning',
    license='MIT',
    platforms='any',
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.3'
    ],
    setup_requires=[],
    install_requires=[
        'cython',
        'numpy'
    ],
    ext_modules=cythonize("glove/glove_inner.pyx"),
    include_package_data=True,
)
