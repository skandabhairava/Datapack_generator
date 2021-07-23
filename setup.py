import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="commandblockpy",
    version="0.0.1",
    author="Terroid#0490 and Anthony2be#1900",
    author_email="skandabhairava@gmail.com and adubovitsky1234@gmail.com",
    description="Datapack Creator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/skandabhairava/Datapack_generator",
    project_urls={
        "Bug Tracker": "https://github.com/skandabhairava/Datapack_generator/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
)