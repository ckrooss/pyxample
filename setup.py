#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='pyxample',
    version="0.1.0",
    description='Full blown python example project',
    packages=['pyxample', 'pyxample.lib'],
    install_requires=['requests',
                      'systemd;platform_system=="linux2"'],
    python_requires='>=2.7',
    test_suite='nose.collector',
    tests_require=['nose', 'coverage', 'hypothesis'],
    setup_requires=['nose', 'coverage', 'hypothesis'],
    author='Christopher Krooß',
    author_email='c.krooss@gmail.com',
    entry_points={
        'console_scripts':
            {
                "pyx = pyxample.pyxample:cli",
            }
    }
)
