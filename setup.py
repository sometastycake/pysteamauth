import setuptools
from setuptools import setup


requirements = [
    'aiohttp>=3.6.0',
    'protobuf>=4.21.1',
    'pydantic>=1.8.1',
    'rsa>=4.8',
    'bitstring>=3.1.9',
]


setup(
    name='pysteamauth',
    version='0.0.3',
    url='https://github.com/sometastycake/pysteamauth',
    license='MIT',
    author='Mike M',
    author_email='stopthisworldplease@outlook.com',
    description='Asynchronous python library for Steam authorization using protobuf',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    zip_safe=False,
    python_requires='>=3.7',
    install_requires=requirements,
    setup_requires=requirements,
    include_package_data=True,
)
