from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='ga-storage-manager',
    version='1.0.1',
    packages=['ga_storage_manager'],
    url='https://github.com/geraldoandradee/ga-storage-manager',
    license='MIT',
    author='Geraldo Andrade',
    author_email='geraldo@geraldoandrade.com',
    description='This is a (POC) simple json storage manager.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
