# Welcome to geomaroc

![geomaroc_logo](https://user-images.githubusercontent.com/49843367/164335838-537f0514-ce89-43ed-956f-c6c6de6ed264.png)


**A Python library to make working with geospatial data of Morocco easier.**

-   GitHub repo: <https://github.com/AmineAndam04/geomaroc>
-   PyPI: <https://pypi.org/project/geomaroc/>
-   Raw data: <https://github.com/AmineAndam04/geomaroc-Raw-data>
## Introduction

People who work in data science are seeing  increased need to work with geospatial data, especially for visualization purposes (e.g. during the covid-19 pandemic).Geopandas is a very popular geospatial library in python that extends Pandas to allow spatial operations on geometrics types.

Working with geopands requires having access to coordinates of the items of our map (polygon coordinates), but having accesss to those coordinates is not an easy task.In fact, we often need the shapefiles in order to plot a map. Trying to find those shapefiles can be a long journey, especailly for someone with zero experience with geospatial data. Moreover, for someone interested in the  geospatial data of Morocco, the majority of shapefiles available online are either of very poor quality, or they don't provide province-level,prefectue-level or district-level coordinates.Even if we manage to find the appropriate shapefiles, they usually come without the southern regions of Morocco.

**Geomaroc** helps the user get those coordinates easly.This library aims to fix these problem by:

     1. providing methods to automatically get the boundary coordinates to plot maps of Morocco **without having acces to shapefiles.**
      
     2. providing access to the coordinates of low-level administrative subdivisions (e.g. province, prefecture, districs).
      
     3. providing access to the complete map of  Morocco (including the southern regions of Morocco)

**illustration:**

![pic2](https://user-images.githubusercontent.com/49843367/164767535-ed77f71a-6610-4abc-a9f9-bb5c54ed4890.png)


## Requirements
geomaroc library needs the following packages :**pandas**, **geopandas**, **shapely**, **json** and **importlib**.
## Install
soon
## gallery

![pic2](https://user-images.githubusercontent.com/49843367/164767535-ed77f71a-6610-4abc-a9f9-bb5c54ed4890.png)
![pic3](https://user-images.githubusercontent.com/49843367/164767545-31ebbdd9-49ff-472e-a396-7e94c2964547.png)
![pic4](https://user-images.githubusercontent.com/49843367/164767547-4e9f179e-1e8b-4478-b099-ff9d93d92b2c.png)
![pic5](https://user-images.githubusercontent.com/49843367/164767553-00114d1f-17d5-4b1e-994b-0d7f9642235e.png)
![pic1](https://user-images.githubusercontent.com/49843367/164767555-e9acaa22-9891-40c2-a7b3-37726c985746.png)
## Raw data
