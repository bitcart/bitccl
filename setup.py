import importlib

from setuptools import find_packages, setup

# Load version.py without importing __init__.py and it's dependencies
# https://docs.python.org/3/library/importlib.html#importing-a-source-file-directly
spec = importlib.util.spec_from_file_location("version", "bitccl/version.py")
version_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(version_module)

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("requirements.txt") as requirements_file:
    requirements = requirements_file.read()

setup(
    author="MrNaif2018",
    author_email="chuff184@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    description="The BitCCL scripting language compiler package",
    entry_points={"console_scripts": ["bitccl=bitccl.cli:main"]},
    install_requires=requirements,
    license="MIT",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords=["bitcartcc", "bitccl", "programminglanguage", "compiler"],
    name="bitccl",
    packages=find_packages(),
    url="https://github.com/bitcartcc/bitccl",
    version=version_module.VERSION,
    zip_safe=False,
    python_requires=">=3.8",
)
