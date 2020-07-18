from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("requirements.txt") as requirements_file:
    requirements = requirements_file.read()

setup(
    author="MrNaif2018",
    author_email="chuff184@gmail.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
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
    url="https://github.com/MrNaif2018/bitccl",
    version="0.0.2",
    zip_safe=False,
)
