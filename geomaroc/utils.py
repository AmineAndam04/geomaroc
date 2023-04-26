import json
import importlib.resources


def regionById(id_region):
    path=importlib.resources.open_text("geomaroc.data", "region_id.json").name
    ids=open(path)
    idx=json.load(ids)
    ids.close
    keys=list(idx.keys())
    vals=list(idx.values())
    return keys[vals.index(id_region)]
def getCoord(cords):
    xy=[]
    x=list(map(lambda x: float(x),cords[0]))
    y=list(map(lambda x: float(x),cords[1]))
    for i in range(len(x)):
        xy.append([x[i],y[i]])
    return [[xy]]

def getPathRegion(n_region=None,id_region=None):
    if n_region!=None:
        file=n_region+".json"
        path=importlib.resources.open_text("geomaroc.data.region", file).name
        return path
    elif n_region==None and id_region!=None :
        file=regionById(id_region)+".json"
        path=importlib.resources.open_text("geomaroc.data.region", file).name
        return path

def getProvById(id_province):
    path=importlib.resources.open_text("geomaroc.data", "prov_id.json").name
    f = open(path)
    prov_id = json.load(f)
    f.close()
    keys=list(prov_id.keys())
    vals=list(prov_id.values())
    return keys[vals.index(id_province)]
def getPathProvince(n_province=None,id_province=None):
    if n_province!=None:
        path=importlib.resources.open_text("geomaroc.data", "prov_region.json").name
        f = open(path)
        prov_region = json.load(f)
        f.close()
        n_region=prov_region[n_province]
        folder="geomaroc.data."+n_region
        file=n_province+".json"
        path_r=importlib.resources.open_text(folder, file).name
        return path_r
    elif n_province==None and id_province!=None :
        n_prov=getProvById(id_province)
        return getPathProvince(n_prov)
def Regions():
    path=importlib.resources.open_text("geomaroc.data", "region_id.json").name
    ids=open(path)
    region=json.load(ids)
    ids.close
    return region
def Provinces():
    path=importlib.resources.open_text("geomaroc.data", "region_prov.json").name
    ids=open(path)
    region=json.load(ids)
    ids.close
    return region