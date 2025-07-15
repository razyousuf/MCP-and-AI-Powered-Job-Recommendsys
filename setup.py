from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "MCP and AI Powered Job Recommender System"
AUTHOR_USER_NAME = "Raz Yousufi"
SRC_REPO = "job_recommender"
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.0",
    author="Raz Yousufi",
    author_email="razyousufi350@gmail.com",
    description="GenAI-powered Job Recommender System using MCP",
    keywords=["GenAI", "Job Recommendation", "MCP"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/razyousuf/MCP-and-AI-Powered-Job-Recommendsys",
    packages=find_packages(),
    license="MIT",
    python_requires=">=3.10",
    install_requires=LIST_OF_REQUIREMENTS
)
