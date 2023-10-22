import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="textsummarization",
    version="0.0.1",
    author="ajitk15",
    author_email="ajitk15@gmail.com",
    description="Text Summarization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ajitk15/ml_text_summarization",
    project_urls={
        "Bug Tracker": "https://github.com/ajitk15/ml_text_summarization/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)