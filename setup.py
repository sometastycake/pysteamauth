from setuptools import setup


setup(
    name='pysteamauth',
    version='0.0.2',
    url='https://github.com/sometastycake/pysteamauth',
    license='MIT',
    author='Mike M',
    author_email='stopthisworldplease@outlook.com',
    description='Asynchronous python library for Steam authorization using protobuf',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=open('requirements.txt').read(),
    zip_safe=False,
    python_requires='>=3.6'
)
