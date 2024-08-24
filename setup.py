from setuptools import setup, find_packages

setup(
    name='all-parser',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        'click',
        'python-docx',
        'PyPDF2',
        'PyYAML',
    ],
    entry_points={
        'console_scripts': [
            'all-parser=all_parser.cmd:parse',
        ],
    },
)
