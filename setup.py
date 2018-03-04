from setuptools import setup
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sample',  # Required
    version='1.0.0',  # Required
    description='A sample Python project',  # Required
    long_description=long_description,  # Optional
    url='https://github.com/locvx1234/sample-tox',  # Optional
    author='LocVU',  # Optional
    author_email='locvx1234@gmail.com',  # Optional
    extras_require={
        'dev': [
            'pytest>=3',
            'tox',
        ],
    },
    classifiers=[  # Optional
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='tox sample setuptools development',  # Optional
    packages=['maths'],
)
