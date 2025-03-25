# setup.py
from setuptools import setup, find_packages
from pathlib import Path

# Read requirements from single requirements.txt file
def read_requirements(filename: str = './requirements/base.txt') -> list[str]:
    return [line.strip() 
            for line in Path(filename).read_text().splitlines()
            if line.strip() and not line.startswith('#')]

# Read long description from README
long_description = Path('README.md').read_text(encoding='utf-8')

setup(
    name="herpai",
    version="0.1.0",
    description="AI-driven discovery platform for HSV cure research",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="OpenBioCure",
    author_email="openbiocure@gmail.com",
    url="https://github.com/openbiocure/HerpAI",
    packages=find_packages(exclude=["tests*"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    entry_points={
        "console_scripts": [
            "herpai=herpai.orchestrator.run:main",
            "herpai-ingest=herpai.ingestion.run_ingestor:main"
        ],
    },
    include_package_data=True,
    package_data={
        'herpai': [
            'configs/*.yaml'
        ],
    },
)