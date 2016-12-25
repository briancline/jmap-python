import setuptools


setuptools.setup(
    name='jmap',
    version='0.0.1',
    description='A pure-Python implementation of the JMAP protocol',
    author='Brian Cline',
    author_email='brian.cline@gmail.com',
    url='https://github.com/briancline/jmap',
    packages=setuptools.find_packages(),
    install_requires=open('requirements.txt', 'r').readlines(),
    namespace_packages=[],
    entry_points={}
)
