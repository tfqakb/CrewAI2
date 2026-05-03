from setuptools import find_packages, setup

setup(
name="mcqgenerator",
version="0.0.1",
author="taufique",
author_email="taufiqueakbar@gmail.com",
install_requires=[
    "langchain",
    "streamlit",
    "python-dotenv",
    "langgraph",
    "crewai",
    "langchain-core",
    "langchain-community",
    "langchain-groq",
    "langchain-classic",
    "Pydantic",
    "PyPDF2",
    "langchain-experimental",
    "langchain-tavily",
    "langchain-huggingface",
    "uvicorn",
    "requests"
],
packages=find_packages()

)