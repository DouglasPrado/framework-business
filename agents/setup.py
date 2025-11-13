"""
Setup configuration for framework-business agents package.
"""
from setuptools import setup, find_packages

setup(
    name="framework-business-agents",
    version="0.1.0",
    description="AI Agent Operating Framework for Business Process Automation",
    author="Framework Business",
    python_requires=">=3.9",
    packages=find_packages(include=["agents", "agents.*"]),
    install_requires=[
        "langchain>=0.1.0",
        "langchain-openai>=0.1.6",
        "langgraph>=0.0.40",
        "python-dotenv>=1.0.0",
        "tavily-python>=0.3.0",
        "pyyaml>=6.0",
        "rich>=13.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "run-strategy=agents.scripts.run_strategy_agent:main",
        ],
    },
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
)
