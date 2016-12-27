import setuptools

import jmap


setuptools.setup(
    name='jmap',
    version=jmap.VERSION,
    description='A pure-Python implementation of the JMAP protocol',
    author='Brian Cline',
    author_email='brian.cline@gmail.com',
    url='https://github.com/briancline/jmap',
    packages=setuptools.find_packages(),
    install_requires=open('requirements.txt', 'r').readlines(),
    namespace_packages=[],
    entry_points={}
)
