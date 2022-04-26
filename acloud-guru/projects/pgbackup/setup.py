from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pgbackup',
    versiom='0.1.0',
    author='Wilton Paulo',
    author_email='wilton@wpstec.com'
    description="A utility for backing up Pgsl databases."
    long_description=long_description,
    long_description='text/markdown',
    url='https://github.com/todo/todo',
    packages=find_packages('src')
)
