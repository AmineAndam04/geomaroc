## 👋👋 We are looking for volunteers who are interested in taking over the maintenance and development of this library. If you are interested in contributing, please reach out to us or create an issue on GitHub to express your interest.

# Welcome to geomaroc

![geomaroc_logo](https://user-images.githubusercontent.com/49843367/164335838-537f0514-ce89-43ed-956f-c6c6de6ed264.png)


**A Python library to make working with geospatial data of Morocco easier.**

-   GitHub repo: <https://github.com/AmineAndam04/geomaroc>
-   PyPI: <https://pypi.org/project/geomaroc/>
-   Raw data: <https://github.com/AmineAndam04/geomaroc-Raw-data>
-   R version: https://github.com/AmineAndam04/R-geomaroc
-   CRAN: https://CRAN.R-project.org/package=geomaroc
## Introduction

People who work in data science are seeing  increased need to work with geospatial data, especially for visualization purposes (e.g. during the covid-19 pandemic).Geopandas is a very popular geospatial library in python that extends Pandas to allow spatial operations on geometrics types.

Working with geopands requires having access to coordinates of the items of our map (polygon coordinates), but having accesss to those coordinates is not an easy task.In fact, we often need the shapefiles in order to plot a map. Trying to find those shapefiles can be a long journey, especailly for someone with zero experience with geospatial data. Moreover, for someone interested in the  geospatial data of Morocco, the majority of shapefiles available online are either of very poor quality, or they don't provide province-level,prefectue-level or district-level coordinates.Even if we manage to find the appropriate shapefiles, they usually come without the southern regions of Morocco.

**Geomaroc** helps the user get those coordinates easly.This library aims to fix these problem by:

     1. providing methods to automatically get the boundary coordinates to plot maps of Morocco **without having acces to shapefiles.**
      
     2. providing access to the coordinates of low-level administrative subdivisions (e.g. province, prefecture, districs).
      
     3. providing access to the complete map of  Morocco (including the southern regions of Morocco)

**illustration:**

To generate those plots go to [Gallery](https://github.com/AmineAndam04/geomaroc/tree/main/geomaroc)

![pic2](https://user-images.githubusercontent.com/49843367/164767535-ed77f71a-6610-4abc-a9f9-bb5c54ed4890.png)


## Requirements
geomaroc library needs the following packages :**pandas**, **geopandas**, **shapely**, **json** and **importlib**.
## Install
```python
pip install geomaroc
import geomaroc 
```
## Usage
-   getRegion() :Helps to plot the shape of each region.
```python
import geomaroc
## working with n_region
gp=geomaroc.getRegion("Casablanca-Settat")
gp.plot()
## working with id_region
gp=geomaroc.getRegion(id_region=6) # Attention!! don't write geomaroc.getRegion(6)
gp.plot()
```

-   getMultiRegion() :Helps to plot the shape of multiple regions.
```python
import geomaroc
## working with n_region
gp=geomaroc.getMultiRegion(["Casablanca-Settat",Draa-Tafilalet])
gp.plot()
## working with id_region
gp=geomaroc.getMultiRegion(id_region=[6,8]) 
gp.plot()
```
-   getProvince() :Helps to plot the shape of provinces within a region.
```python
import geomaroc
## working with n_region
gp=geomaroc.getProvince("Casablanca-Settat")
gp.plot()
## working with id_region
gp=geomaroc.getProvince(id_region=6)
gp.plot()
```
-   getMultiProvince(): Helps to plot the shape of provinces in multiple regions.
```python
import geomaroc
## working with n_region
gp=geomaroc.getMultiProvince(["Casablanca-Settat",Draa-Tafilalet])
gp.plot()
## working with id_region
gp=geomaroc.getMultiProvince(id_region=[6,8])
gp.plot()
```
-   getDistrict(): Helps to plot the shape of districts within a province.
```python
import geomaroc
## working with n_province
geomaroc.getDistrict("Tetouan")
gp.plot()
## working with id_province
gp=geomaroc.getProvince(id_region=571)
gp.plot()
```
-   getMultiDistrict(): Helps to plot the shape of districts in multiple provinces.
```python
import geomaroc
## working with n_province
gp=geomaroc.gp=geomaroc.getMultiDistrict(["Tetouan","Tanger-Assilah","Al-Hoceima"])
gp.plot()
## working with id_province
gp=geomaroc.geomaroc.getProvince(id_region=[571,51,511])
gp.plot()
```
-  Regions() & Provinces() : Hepls to respect the notation and to get the id of each region and province

## Notation 
We adpoted this methode to work with names and id of regions,provinces and districts :
- replace "é" with "e"
- replace "è" with "e"
- replace " " with "-"
- replace "â" with "a"
- 
So "Tanger-Tétouan-Al Hoceima" becomes "Tanger-Tetouan-Al-Hoceima" and "Drâa-Tafilalet" becomes "Drâa-Tafilalet"

Use geomaroc.Regions() and geomaroc.Provinces() to check the notations:
```python
region=geomaroc.Regions()
region
```

```{r, engine='python', count_lines}
{'Beni-Mellal-Khenifra': 5,
 'Casablanca-Settat': 6,
 'Draa-Tafilalet': 8,
 'Eddakhla-Oued-Eddahab': 12,
 'Fes-Meknes': 3,
 'Guelmim-Oued-Noun': 10,
 'Laayoune-Sakia-El-Hamra': 11,
 'Marrakech-Safi': 7,
 'Oriental': 2,
 'Rabat-Sale-Kenitra': 4,
 'Souss-Massa': 9,
 'Tanger-Tetouan-Al-Hoceima': 1}
 
 ```
 ```python
 import pandas as pd
provinces=geomaroc.Provinces()
province=pd.DataFrame(columns=["Region","Id_region","Province","Id_province"])
for i in range(len(provinces.keys())):
    for j in range(len(provinces[list(provinces.keys())[i]])):
        reg=list(provinces.keys())[i]
        prov=list(provinces[reg].keys())[j]
        province=province.append({"Region":reg,"Id_region":region[reg],"Province":prov,"Id_province":provinces[reg][prov]},ignore_index=True)
province
```

```{r, engine='python', count_lines}
	Region	                 Id_region	Province	Id_province
0	Beni-Mellal-Khenifra	     5	     Khouribga	      311
1	Beni-Mellal-Khenifra	     5	     Khenifra	      301
2	Beni-Mellal-Khenifra	     5	     Azilal	      81
3	Beni-Mellal-Khenifra	     5	     Beni-Mellal	 91
4	Beni-Mellal-Khenifra	     5	     Fquih-Ben-Salah 255
...	...	...	...	...
70	Tanger-Tetouan-Al-Hoceima	1	     Mdiq-Fnidq	 573
71	Tanger-Tetouan-Al-Hoceima	1	     Ouezzane	      405
72	Tanger-Tetouan-Al-Hoceima	1	     Tanger-Assilah	 511
73	Tanger-Tetouan-Al-Hoceima	1	     Tetouan	      571
74	Tanger-Tetouan-Al-Hoceima	1	     Al-Hoceima	 51
 ```    

## Raw data
Visit [geomaroc raw data](https://github.com/AmineAndam04/geomaroc-Raw-data)
## gallery

![pic2](https://user-images.githubusercontent.com/49843367/164767535-ed77f71a-6610-4abc-a9f9-bb5c54ed4890.png)
![pic3](https://user-images.githubusercontent.com/49843367/164767545-31ebbdd9-49ff-472e-a396-7e94c2964547.png)
![pic4](https://user-images.githubusercontent.com/49843367/164767547-4e9f179e-1e8b-4478-b099-ff9d93d92b2c.png)
![pic5](https://user-images.githubusercontent.com/49843367/164767553-00114d1f-17d5-4b1e-994b-0d7f9642235e.png)
![pic1](https://user-images.githubusercontent.com/49843367/164767555-e9acaa22-9891-40c2-a7b3-37726c985746.png)
