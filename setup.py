from setuptools import setup, find_packages

setup(
    name='songsterr_to_gp',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'tqdm',
        'lxml'
    ],
    entry_points={
        'console_scripts': [
            'songsterr-to-gp=songsterr_to_gp.downloader:main',
        ],
        'console_scripts': [
            'songsterr-to-gp=songsterr_to_gp.downloader:main',
        ],
    },

    author='',
    author_email='',
    description='A script to download tabs from Songsterr as Guitar Pro files',
    keywords='guitar tab downloader music song songsterr',
    url='',  
)
