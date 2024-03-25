from setuptools import setup, find_packages

setup(
    name='drivers',
    license='BSD-3-Clause',
    url='https://qiime2.org',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'qiime2',
    ]
)
