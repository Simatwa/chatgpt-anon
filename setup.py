from pathlib import Path

from setuptools import setup


DOCS_PATH = Path(__file__).parents[0] / "docs/README.md"
PATH = Path("README.md")
if not PATH.exists():
    with Path.open(DOCS_PATH, encoding="utf-8") as f1:
        with Path.open(PATH, "w+", encoding="utf-8") as f2:
            f2.write(f1.read())

setup(
    name="chatgpt-anon",
    version="0.0.1",
    license="GNU v3",
    author="Smartwa",
    maintainer="Smartwa",
    author_email="simatwacaleb@proton.me",
    description="Intreract with ChatGPT anonymously.",
    packages=["chatgpt_anon"],
    url="https://github.com/Simatwa/chatgpt-anon",
    project_urls={
        "Bug Report": "https://github.com/Simatwa/chatgpt-anon/issues/new",
        "Homepage": "https://github.com/Simatwa/chatgpt-anon",
        "Source Code": "https://github.com/Simatwa/chatgpt-anon",
        "Issue Tracker": "https://github.com/Simatwa/chatgpt-anon/issues",
        "Download": "https://github.com/Simatwa/chatgpt-anon/releases",
        "Documentation": "https://github.com/Simatwa/chatgpt-anon/blob/main/docs/README.md",
    },
    entry_points={
        "console_scripts": [
            "chatgpt-anon = chatgpt_anon.console:main",
            "cga = chatgpt_anon.console:main",
        ],
    },
    install_requires=[
        "requests==2.31.0",
        "python-dotenv==1.0.0",
        "click==8.1.3",
        "rich==13.3.4",
        "clipman==3.1.0",
        "pyperclip==1.8.2",
    ],
    python_requires=">=3.10",
    keywords=[
        "chatgpt",
        "chatgpt-anon",
        "gpt",
        "chatgpt-cli",
        "chatgpt-sdk",
        "chatgpt-api",
    ],
    long_description=Path.open(PATH, encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Intended Audience :: Developers",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: Free For Home Use",
        "Intended Audience :: Customer Service",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
