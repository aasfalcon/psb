import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'Sample Browser',
    version = '0.1.1',
    author = "Andy S.",
    author_email = "andrewjcarter@gmail.com",
    packages = ['main'],
    include_package_data = True,
    zip_safe = False,
    description = ("Simple sound file browser and previewer."),
    long_description = read('README.md'),
    license = "BSD",
    keywords = "wav sample player file browser",
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
        "Environment :: X11 Applications :: Qt",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Multimedia :: Sound/Audio :: Players",
    ],
    install_requires = [
        'JACK-client',
        'numpy',
        'soundfile',
        'scikits.samplerate'
    ]
)
