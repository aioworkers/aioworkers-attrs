#!/usr/bin/env python

from setuptools import setup, find_packages

package = 'aioworkers_attrs'

requirements = [
    'aioworkers>=0.10.0',
    'attrs',
]

setup(
    name='aioworkers-attrs',
    version='0.0.1',
    description="",
    author="Alexander Malev",
    author_email='yttrium@somedev.ru',
    url='https://github.com/aioworkers/aioworkers-attrs',
    packages=[i for i in find_packages() if i.startswith(package)],
    include_package_data=True,
    install_requires=requirements,
    license="Apache Software License 2.0",
    keywords='aioworkers attrs',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
