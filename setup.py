#! /usr/bin/env python3

"""
Setup script for djerba-benchmark
"""

from setuptools import setup, find_packages

with open('src/lib/djerba_benchmark/version.py') as version_file:
    exec(version_file.read()) # sets __version__
package_root = 'src/lib'

# list of wildcards, intended to capture ancillary files for plugins/helpers/mergers
# TODO make this neater and/or introduce stronger naming conventions
install_wildcards = [
    '*.bed',
    '*.ini',
    '*.json',
    '*.html',
    '*.txt',
    '*.r',
    '*.R',
    'data/*',
    'html/*',
    'resources/*',
    'R/*',
    'r/*',
    'Rscripts/*',
    'templates/*'
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='djerba',
    version=__version__,
    scripts=[
        'src/bin/benchmark.py',
    ],
    packages=find_packages(where=package_root),
    package_dir={'' : package_root},
    package_data={
        'djerba_benchmark': [
            'util/ini/benchmark_pwgs.ini',
            'util/ini/benchmark_tar.ini',
            'util/ini/benchmark_wgs.ini',
            'util/ini/benchmark_wgts.ini',
        ],
        'djerba_benchmark.plugins.benchmark': install_wildcards,
    },
    install_requires=[
        'configparse',
        'mako',
    ],
    python_requires='>=3.10.6',
    author="Iain Bancarz",
    author_email="ibancarz [at] oicr [dot] on [dot] ca",
    description="Benchmarking for Djerba reports",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/oicr-gsi/djerba",
    keywords=['cancer', 'bioinformatics'],
    license='GPL 3.0',
)
