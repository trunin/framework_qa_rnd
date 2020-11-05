import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='framewor_qa_rnd',
    version="0.0.3",
    author='e.trunin',
    author_email='e.trunin@corp.mail.ru',
    description="qa framework for rnd team",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/trunin/framewor_qa_rnd',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)