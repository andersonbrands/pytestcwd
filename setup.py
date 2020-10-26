from pathlib import Path
import setuptools

setuptools.setup(
    name='pytestcwd',
    version='version: 0.1.0'.replace('version: ', ''),
    author='Anderson Brandao',
    author_email='anderson.brands@gmail.com',
    description='',
    long_description=Path('README.md').read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/andersonbrands/pytestcwd",
    packages=setuptools.find_packages(),
    install_requires=[
        'pytest',
    ],
    entry_points={
        'console_scripts': ['pytestcwd=pytestcwd.__main__:console_script_entry']
    },
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
)
