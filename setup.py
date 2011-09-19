# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

long_desc = '''
This package contains the sphinxcontrib-templatehelper Sphinx extension.

This extension is a helper for creating your own template.
'''

requires = ['Sphinx>=0.6']

setup(
    name='sphinxcontrib-templatehelper',
    version='0.1',
    url='http://aohta.github.com/sphinxcontrib-templatehelper',
    #download_url='http://pypi.python.org/pypi/sphinxcontrib-${name}',
    license='BSD',
    author='aohta',
    author_email='fire.kuma8+github2@gmail.com',
    description='Sphinx "sphinxcontrib-templatehelper" extension',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
