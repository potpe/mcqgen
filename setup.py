from setuptools import find_packages, setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='potpe (course by Sunny Savita)',
    author_email='not@provided.email',
    install_requires=["openai", "langchain", "streamlit", "python-dotenv", "PyPDF2"],
    packages=find_packages()
)