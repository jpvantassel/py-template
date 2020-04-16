"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
with open("README.md", encoding="utf8") as f:
    long_description = f.read()

setup(
    name='package',
    version='0.1.0',
    description='',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    author='',
    author_email='',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',

        'Topic :: Education',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Physics',

        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='',
    packages=find_packages(),
    python_requires = '>=3.6, <3.9',
    install_requires=['numpy'],
    extras_require={
        'dev': [],
    },
    package_data={
    },
    data_files=[
        ],
    entry_points={
    },
    project_urls={ 
        'Bug Reports': '',
        'Source': '',
        'Docs': '',
    },
)