from setuptools import setup, find_packages

setup(
    name="qmemcalc",
    version="0.1.0",
    author="Sachin",
    author_email="sachin18449kumar@gmail.com",
    description="GPU Memory Estimator for QLoRA / LoRA / Transformers",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "torch>=2.0",
        "transformers>=4.40",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
