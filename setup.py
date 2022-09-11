import setuptools
from setuptools import setup


requirements = [
    'aiohttp>=3.8.1',
    'protobuf>=4.21.5',
    'pydantic>=1.10.2',
    'rsa>=4.9',
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
