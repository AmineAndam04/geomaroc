# Welcome to geomaroc

![geomaroc_logo](https://user-images.githubusercontent.com/49843367/164335838-537f0514-ce89-43ed-956f-c6c6de6ed264.png)


**A Python library to make working with geospatial data of Morocco easier.**

-   GitHub repo: <https://github.com/AmineAndam04/geomaroc>
-   PyPI: 
-   Raw data: <https://github.com/AmineAndam04/geomaroc-Raw-data>
## Introduction

People who work in data science are seeing  increased need to work with geospatial data, especially for visualization purposes (e.g. during the covid-19 pandemic).Geopandas is a very popular geospatial library in python that extends Pandas to allow spatial operations on geometrics types.

Working with geopands requires having access to coordinates of the items of our map (polygon coordinates), but having accesss to those coordinates is not an easy task.In fact, we often need the shapefiles in order to plot a map. Trying to find those shapefiles can be a long journey, especailly for someone with zero experience with geospatial data. Moreover, for someone interested in the  geospatial data of Morocco, the majority of shapefiles available online are either of very poor quality, or they don't provide province-level,prefectue-level or district-level coordinates.Even if we manage to find the appropriate shapefiles, they usually come without the southern regions of Morocco.

**Geomaroc** helps the user get those coordinates easly.This library aims to fix these problem by:

     1. providing methods to automatically get the boundary coordinates to plot maps of Morocco **without having acces to shapefiles.**
      
     2. providing access to the coordinates of low-level administrative subdivisions (e.g. province, prefecture, districs).
      
     3. providing access to the complete map of  Morocco (including the southern regions of Morocco)

**illustration:**

![geomaroc_illustration](https://user-images.githubusercontent.com/49843367/164404630-164f6edf-8009-4446-9eb3-8974d2ca2ec9.png)



## Requirements
geomaroc library needs the following packages :**pandas**, **geopandas**, **shapely**, **json** and **importlib**.
## Install
soon

## Raw data
