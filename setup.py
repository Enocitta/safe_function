from pathlib import Path
from setuptools import setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

VERSION = '0.0.1'
DESCRIPTION = 'Function decorator to debug Type Errors in runtime calls'
PACKAGE_NAME = 'safe_function'
AUTHOR = 'Ezequiel O G.Nocitta'
EMAIL = 'goegutierrez@gmail.com'
GITHUB_URL = 'https://github.com/Enocitta'

setup(
    name=PACKAGE_NAME,
    packages=[PACKAGE_NAME],
    version=VERSION,
    license='GPLv3',
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    author=AUTHOR,
    author_email=EMAIL,
    url=GITHUB_URL,
    keywords=[],
    install_requires=[
        'nose',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Bug Tracking',
        'License :: OSI Approved ::  GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
    ],
)
