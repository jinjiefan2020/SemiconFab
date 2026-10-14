from setuptools import setup, find_packages

setup(
    name="mimac2026",
    version="1.0.0",
    description="MIMAC-2026: 300mm Wafer Fab Simulation Benchmark & Gym API",
    packages=find_packages(),
    install_requires=[
        "simpy>=4.0.0",
        "numpy>=1.22.0",
    ],
    extras_require={
        "test": ["pytest>=7.0.0"],
    },
    python_requires=">=3.9",
)
