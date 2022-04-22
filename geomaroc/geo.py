import pandas as pd
import geopandas as gpd
from shapely.geometry import shape
from .utils import *


def getRegion(n_region=None,id_region=None):
    """
    Helps to plot the shape of each region.
    Inputs:
           - n_region (string) : The name of the region to plot. The notation should be respected.
                        To get the notation execute: geomaroc.Regions()
           - id_region (int) : Each region has an id. To get the id of each region please execute
                         geomaroc.Regions()
    Outout: 
           - geopandas dataframe

    Example:
           ---> import geomaroc
           ---> ## working with n_region
           ---> gp=geomaroc.getRegion("Casablanca-Settat")
           ---> gp.plot()
           ---> ## working with id_region
           ---> gp=geomaroc.getRegion(id_region=6) # Attention!! don't write geomaroc.getRegion(6)
           ---> gp.plot()

    """
    if n_region==None and id_region==None:
        print("getRegion() require n_region or id_region")
        return 0
    elif n_region==None and id_region!=None:
        n_region=regionById(id_region)
    path=importlib.resources.open_text("geomaroc.data", "Maroc.json").name
    f = open(path)
    row_data = json.load(f)[n_region]
    f.close()
    row_data["libelle_fr"]=row_data["libelle_fr"].replace("é","e").replace("è","e").replace("â","a").replace(" ","-")
    xy=getCoord(row_data["Coordinates"])
    row_data["Coordinates"]=shape({"type":"MultiPolygon","coordinates":xy})
    df=pd.DataFrame(row_data)
    return gpd.GeoDataFrame(df, geometry='Coordinates')

def getMultiRegion(n_region=None,id_region=None):
    """
    Helps to plot the shape of multiple regions.
    Inputs:
           - n_region (list of string) :The names of region to plot. The notation should be respected.
                        To get the notation execute: geomaroc.Regions()
           - id_region (list of int) : List of region ids.Each region has an id.
                                       To get the id of each region please execute geomaroc.Regions()
    Outout: 
           - geopandas dataframe

    Example:
           ---> import geomaroc
           ---> ## working with n_region
           ---> gp=geomaroc.getMultiRegion(["Casablanca-Settat",Draa-Tafilalet])
           ---> gp.plot()
           ---> ## working with id_region
           ---> gp=geomaroc.getMultiRegion(id_region=[6,8]) # Attention!! don't write geomaroc.getMultiRegion([6,8])
           ---> gp.plot()

    """
    if n_region!=None and type(n_region)==list:
        gp=[]
        for region in n_region:
            gp.append(getRegion(region))
        return pd.concat(gp,ignore_index=True)
    elif n_region==None and id_region!=None and type(id_region)==list:
        gp=[]
        for idx in id_region:
            gp.append(getRegion(id_region=idx))
        return pd.concat(gp,ignore_index=True)
    else:
        print("Error in arguments")
        return 0


def getProvince(n_region=None,id_region=None):
    """
    Helps to plot the shape of provinces within a region.
    Inputs:
           - n_region (string) : The name of the region to plot. The notation should be respected.
                        To get the notation execute: geomaroc.Regions()
           - id_region (int) : Each region has an id. To get the id of each region please execute
                         geomaroc.Regions()
    Outout: 
           - geopandas dataframe

    Example:
           ---> import geomaroc
           ---> ## working with n_region
           ---> gp=geomaroc.getProvince("Casablanca-Settat")
           ---> gp.plot()
           ---> ## working with id_region
           ---> gp=geomaroc.getProvince(id_region=6) # Attention!! don't write geomaroc.getProvince(6)
           ---> gp.plot()

    """
    if n_region==None and id_region==None:
        print("getRegion() require n_region or id_region")
        return 0
    path=getPathRegion(n_region,id_region)
    f = open(path)
    row_data = json.load(f)["Data"]
    f.close()
    libelle_ar=[]
    libelle_fr=[]
    region_fr=[]
    region_ar=[]
    code_reg=[]
    code_prov=[]
    coord=[]
    for province in row_data:
        libelle_ar.append(province["libelle_ar"])
        libelle_fr.append(province["libelle_fr"].replace("é","e").replace("è","e").replace(" ","-"))
        region_fr.append(province["region_fr"].replace("é","e").replace("è","e").replace(" ","-"))
        region_ar.append(province["region_ar"])
        code_reg.append(int(float(province["code_reg"])))
        code_prov.append(int(float(province["code_prov"])))
        xy=getCoord(province["coordinates"])
        coord.append(shape({"type":"MultiPolygon","coordinates":xy}))
    df=pd.DataFrame(
        {"Province_fr":libelle_fr,
        "Province_ar":libelle_ar,
        "code_prov":code_prov,
        "Region_fr":region_fr,
        "Region_ar":region_ar,
        "code_reg":code_reg,
        "Coordinates":coord})
    return gpd.GeoDataFrame(df, geometry='Coordinates')

def getMultiProvince(n_region=None,id_region=None):
    """
    Helps to plot the shape of provinces in multiple regions.
    Inputs:
           - n_region (list of string) :The names of region to plot. The notation should be respected.
                        To get the notation execute: geomaroc.Regions()
           - id_region (list of int) : List of region ids.Each region has an id.
                                       To get the id of each region please execute geomaroc.Regions()
    Outout: 
           - geopandas dataframe

    Example:
           ---> import geomaroc
           ---> ## working with n_region
           ---> gp=geomaroc.getMultiProvince(["Casablanca-Settat",Draa-Tafilalet])
           ---> gp.plot()
           ---> ## working with id_region
           ---> gp=geomaroc.getMultiProvince(id_region=[6,8]) # Attention!! don't write geomaroc.getMultiProvince([6,8])
           ---> gp.plot()

    """
    if n_region!=None and type(n_region)==list:
        gp=[]
        for region in n_region:
            gp.append(getProvince(region))
        return pd.concat(gp,ignore_index=True)
    elif n_region==None and id_region!=None and type(id_region)==list:
        gp=[]
        for idx in id_region:
            gp.append(getProvince(id_region=idx))
        return pd.concat(gp,ignore_index=True)
    else:
        print("Error in arguments")
        return 0

def getDistrict(n_province=None,id_province=None):
    """
    Helps to plot the shape of districts within a province.
    Inputs:
           - n_province (string) : The name of the province to plot. The notation should be respected.
                        To get the notation execute: geomaroc.Provinces()
           - id_province (int) :the id of the province. Each province has an id. To get the id of each province please execute
                         geomaroc.Provinces()
    Outout: 
           - geopandas dataframe

    Example:
           ---> import geomaroc
           ---> ## working with n_province
           ---> gp=geomaroc.getDistrict("Tetouan")
           ---> gp.plot()
           ---> ## working with id_province
           ---> gp=geomaroc.getProvince(id_region=571) # Attention!! don't write geomaroc.getProvince(6)
           ---> gp.plot()
    """
    if n_province==None and id_province==None:
        print("Arguments error")
        return 0
    path=getPathProvince(n_province,id_province)
    f = open(path)
    row_data = json.load(f)["Data"]
    f.close()
    prov_fr=[]
    prov_ar=[]
    code_prov=[]
    com_fr=[]
    cod_com=[]
    cercle_fr=[]
    cod_cercle=[]
    libelle_ar=[]
    libelle_fr=[]
    region_fr=[]
    region_ar=[]
    code_reg=[]
    coord=[]
    for cercle in row_data:
        prov_fr.append(cercle["prov_fr"].replace("é","e").replace("è","e").replace(" ","-"))
        prov_ar.append(cercle["prov_ar"])
        code_prov.append(int(float(cercle["code_prov"])))
        com_fr.append(cercle["com_fr"])
        cod_com.append(cercle["cod_com"])
        cercle_fr.append(cercle["cercle_fr"])
        cod_cercle.append(cercle["cod_cercle"])
        libelle_ar.append(cercle["libelle_ar"])
        libelle_fr.append(cercle["libelle_fr"].replace("é","e").replace("è","e").replace(" ","-"))
        region_fr.append(cercle["region_fr"].replace("é","e").replace("è","e").replace(" ","-"))
        region_ar.append(cercle["region_ar"])
        code_reg.append(int(float(cercle["code_reg"])))
        xy=getCoord(cercle["Data"])
        coord.append(shape({"type":"MultiPolygon","coordinates":xy}))
    df=pd.DataFrame(
        {"libelle_fr":libelle_fr,
         "libelle_ar":libelle_ar,
         "cercle_fr":cercle_fr,
         "cod_cercle":cod_cercle,
         "com_fr":com_fr,
        "cod_com":cod_com,
        "prov_fr":prov_fr,
        "prov_ar":prov_ar,
        "code_prov":code_prov,
        "region_fr":region_fr,
        "region_ar":region_ar,
        "code_reg":code_reg,
        "Coordinates":coord})
    return gpd.GeoDataFrame(df, geometry='Coordinates') 

def getMultiDistrict(n_province=None,id_province=None):
    """
    Helps to plot the shape of districts of multiple provinces.
    Inputs:
           - n_province (list of string) : The list of the province to plot. The notation should be respected.
                        To get the notation execute: geomaroc.Provinces()
           - id_province (list of int) : Each province has an id. To get the id of each province please execute
                         geomaroc.Provinces()
    Outout: 
           - geopandas dataframe

    Example:
           ---> import geomaroc
           ---> ## working with n_province
           ---> gp=geomaroc.getMultiDistrict(["Tetouan","Tanger-Assilah","Al-Hoceima"])
           ---> gp.plot()
           ---> ## working with id_province
           ---> gp=geomaroc.getProvince(id_region=[571,51,511]) # Attention!! don't write geomaroc.getProvince(6)
           ---> gp.plot()
    """
    if n_province!=None and type(n_province)==list:
        gp=[]
        for prov in n_province:
            gp.append(getDistrict(prov))
        return pd.concat(gp,ignore_index=True)
    elif n_province==None and id_province!=None and type(id_province)==list:
        gp=[]
        for idx in id_province:
            gp.append(getDistrict(id_province=idx))
        return pd.concat(gp,ignore_index=True)
    else:
        print("Error in arguments")
        return 0