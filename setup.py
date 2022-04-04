from setuptools import setup, find_packages

setup(
    name="oderint",
    version="0.0.0",
    description="The execution assistant",
    author="bug3",
    author_email="bug3dev@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "Click",
    ],
    entry_points={
        "console_scripts": [
            "oderint = oderint:cli",
        ],
    },
)
