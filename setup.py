import setuptools
from setuptools import setup


requirements = [
    'aiohttp>=3.8.1',
    'aiosignal>=1.2.0',
    'async-timeout>=4.0.2',
    'attrs>=22.1.0',
    'charset-normalizer>=2.1.1',
    'frozenlist>=1.3.1',
    'idna>=3.3',
    'multidict>=6.0.2',
    'protobuf>=4.21.5',
    'pyasn1>=0.4.8',
    'pydantic>=1.10.2',
    'rsa>=4.9',
    'typing_extensions>=4.3.0',
    'yarl>=1.8.1'
]


setup(
    name='pysteamauth',
    version='0.0.1',
    url='https://github.com/sometastycake/pysteamauth',
    license='MIT',
    author='Mike M',
    author_email='stopthisworldplease@outlook.com',
    description='Asynchronous python library for Steam authorization using protobuf',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    zip_safe=False,
    python_requires='>=3.6',
    install_requires=requirements,
    setup_requires=requirements,
    include_package_data=True,
)
