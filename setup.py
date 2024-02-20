from setuptools import setup, find_packages

setup(
    name='Whoismple',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        're',
        'requests',
    ],
    author='Daniel Szewczuk',
    author_email='daniel@szewczuk.dev',
    description='',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/danielszewczuk/whoisimple',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
