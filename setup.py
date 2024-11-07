from setuptools import setup, find_packages
from pathlib import Path

# version
here = Path(__file__).absolute().parent
version_data = {}
with open(here.joinpath("miguellib", "__init__.py"), "r") as f:
    exec(f.read(), version_data)
version = version_data.get("__version__", "0.0")

install_requires = [
    "numpy>=1.19",  # 1.19 required by tensorflow 2.6
    "pandas>1.0.3,<2",
    "ipykernel>=4.6.1,<7",
    "jupyter>=1,<2",
    "black>=18.6b4,<21",
    "pytest>=3.6.4",
]

setup(
    name="miguellib",
    version=version,
    install_requires=install_requires,
    package_dir={"miguellib": "miguellib"},
    python_requires=">=3.6",
    packages=find_packages(where=".", exclude=["docs", "examples", "tests"]),
)
