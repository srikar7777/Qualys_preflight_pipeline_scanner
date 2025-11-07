from setuptools import setup, find_packages

setup(
    name='pre-flight-scanner',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['aiohttp', 'PyYAML', 'rich'],
    entry_points={
        'console_scripts': [
            'pre-flight-scan=preflight.cli:main',
        ],
    },
)

