import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    README = f.read()

setuptools.setup(
    name="yt_ripper",
    version="0.0.9",
    author="Jonathani Atticus64",
    author_email="jonaenglish64@gmail.com",
    description="Project with Python to download videos and mp3 files of youtube in the terminal", 
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/atticus64/yt_ripper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Topic :: Terminals :: Terminal Emulators/X Terminals"
    ],
    keywords="youtube",
    python_requires='>=3.6',
    install_requires=["colorama", "pytube", "tqdm"],
    include_package_data=True,
    entry_points={
        "console_scripts": ["ytripper = yt_ripper.main:main"]
    },
)
