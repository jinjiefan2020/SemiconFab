from setuptools import setup, find_packages

setup(
    name="schemavalidator",
    version="1.0.0",
    description="Validator and CLI for SemiconFab Equipment Schema v1.0",
    packages=find_packages(),
    package_data={"schemavalidator": ["schema.json"]},
    include_package_data=True,
    install_requires=[
        "jsonschema>=4.18.0",
    ],
    extras_require={
        "test": ["pytest>=7.0.0"],
    },
    entry_points={
        "console_scripts": [
            "schemavalidator=schemavalidator.cli:main",
        ],
    },
    python_requires=">=3.9",
)
