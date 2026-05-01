import pathlib

from setuptools import setup

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

GITHUB_URL = "https://github.com/dheerajreal/random-strings/"
VERSION = '0.2.0'


setup(
    name='random-strings',
    version=VERSION,
    license='MIT',
    description='strings that are ✨ random ✨',
    url=GITHUB_URL,
    keywords=['random', 'strings', 'utilities', 'security'],
    py_modules=["random_strings"],
    python_requires='>=3.6, <4',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
        'Programming Language :: Python :: 3 :: Only'
    ],

    project_urls={
        'Bug Reports': GITHUB_URL + 'issues/',
        'Source': GITHUB_URL,
    },
)
