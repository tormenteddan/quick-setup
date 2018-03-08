"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='piper',
    version='0.1.0',
    description='A custom init script for creating python projects',
    long_description=long_description,
    url='https://github.com/tormenteddan/piper',
    author='Daniel Aragon',
    author_email='daniel.aragon.bermudez@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='init setuptools development script',
    py_modules=['piper'],
    install_requires=['Click'],
    entry_points='''
        [console_scripts]
        piper=piper:cli
        ''',
)
