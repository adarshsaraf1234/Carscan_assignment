import numpy as np 
import pandas as pd 
import sys 
import matplotlib.pyplot as plt
import random
import cv2
from PIL import Image,ImageDraw,ImageFont
import json

base_name="C://Users//Adarsh//Desktop//all_projects//Assignment"
damage_identification="Damage Identification//"
data_viz="Data Visualization//"


def get_json_values(json_file,image_file,opacity):
    jf=open(json_file)
    data=json.load(jf)
    img=Image.open(image_file)
    poly = Image.new('RGBA', img.size)
    pdraw = ImageDraw.Draw(poly)
    height,width=img.size
    viz1,viz2=img,img
    img_copy=img.copy()
    for i in data:
        values=i["value"]
        xmin,ymin,xmax,ymax=0,0,0,0
        
        if "points" and "polygonlabels" in values.keys():
            shape=[]
            points=values["points"]
            labels=values["polygonlabels"]
            denormalized_values=[]
            
            for i in points:
                
                x=(i[0]*height)/100
                y=(i[1]*width)/100
                denormalized_values.append((x,y))
            cup_poly=denormalized_values
            a,b,c=random.randint(0,255),random.randint(0,255),random.randint(0,255)
            
            pdraw.polygon(cup_poly,fill=(a,b,c,int(255*opacity)),outline=(0,0,0,255))
            pdraw.line(cup_poly, fill=(a,b,c),width=3)
            x=[]
            y=[]
            for i in cup_poly:
                x.append(i[0])
                y.append(i[1])
            xmin,ymin,xmax,ymax=min(x),min(y),max(x),max(y)
            shape=[(xmin,ymin),(xmax,ymax)]
            img1=ImageDraw.Draw(img)
            img1.rectangle(shape,outline=(a,b,c))
            img1.text((xmin,ymin),labels[0],fill=(255,255,255))
            
    img_copy.paste(poly,mask=poly)
    img.paste(poly,mask=poly)
    
    return img_copy,img
            
              
