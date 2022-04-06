from setuptools import setup, find_packages

setup(
    name="oderint",
    version="0.0.0",
    description="The execution assistant",
    keywords="automation formatter execution assistant",
    author="bug3",
    author_email="bug3dev@gmail.com",
    url="https://github.com/bug3/oderint",
    license="MIT",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["click", "psutil"],
    entry_points={
        "console_scripts": [
            "oderint = oderint:cli",
        ],
    },
)
