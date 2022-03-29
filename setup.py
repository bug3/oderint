from setuptools import setup, find_packages

setup(
    name="oderint",
    version="0.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Click",
    ],
    entry_points={
        "console_scripts": [
            "oderint = src.main:cli",
        ],
    },
)
