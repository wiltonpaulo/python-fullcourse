from setuptools import setup, find_packages

with open("README.rst", encoding="UTF-8") as f:
    readme = f.read()

setup(
    name="pgbackup",
    version="0.1.0",
    author="Wilton Paulo",
    author_email="wilton@wpstec.com",
    description="A utility for backing up Pgsl databases.",
    long_description=readme,
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=["boto3"],
    python_requires=">=3.8",
    entry_points={"console_scripts": ["pgbackup=pgbackup.cli:main"]},
)
