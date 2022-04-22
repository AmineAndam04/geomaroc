import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="geomaroc",
    version="1.0.1",
    author="ANDAM Amine",
    author_email="andamamine83@gmail.com",
    description='A Python library to easily visualize geospatial data of Morocco.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/AmineAndam04/geomaroc',
    keywords=["geospatial","data visualization","Morocco","data-science","maps"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    include_package_data=True,
    package_data={'':['data/*.json',"data/Beni-Mellal-Khenifra/*.json", "data/Casablanca-Settat/*.json", "data/Draa-Tafilalet/*.json", "data/Eddakhla-Oued-Eddahab/*.json", "data/Fes-Meknes/*.json", "data/Guelmim-Oued-Noun/*.json", "data/Laayoune-Sakia-El-Hamra/*.json", "data/Marrakech-Safi/*.json", "data/Oriental/*.json", "data/Rabat-Sale-Kenitra/*.json", "data/Souss-Massa/*.json", "data/Tanger-Tetouan-Al-Hoceima/*.json","data/region/*.json"]},
)
