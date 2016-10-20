#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='humanhash3',
    version='0.0.5',
    description='Human-readable representations of digests.',
    author='Federico Ficarelli',
    author_email='federico.ficarelli@gmail.com',
    url='https://github.com/nazavode/humanhash',
    py_modules=['humanhash'],
    license='Public Domain',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Security',
        'Topic :: Utilities',

        # Pick your license as you wish (should match "license" above)
        'License :: Public Domain',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
)
