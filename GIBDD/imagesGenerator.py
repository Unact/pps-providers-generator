#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, textgen
from services import services

#FONT_FILE="Play-Bold.ttf"
FONT_FILE="FranklinGothicMediumC.otf"
IMAGE_WIDTH=185
IMAGE_HEIGHT=64

HOME_DIR=os.path.abspath(os.path.dirname(sys.argv[0]))
IMAGES_DIR=os.path.join(HOME_DIR,"images")
FONT_PATH=os.path.join(HOME_DIR,FONT_FILE)

if not os.path.exists(IMAGES_DIR):
    os.makedirs(IMAGES_DIR)

for service in services.itervalues():
    filename=os.path.splitext(service['image'])[0]+'.png'
    filePath=os.path.join(IMAGES_DIR,filename)

    buttonText=service['name']
    buttonText=buttonText.replace('. ','._')
    buttonText=buttonText.replace(' с ','_с_')
    buttonText=buttonText.replace(' и ','_и_')
    buttonText=buttonText.replace('+ ','+_')
    print buttonText

    buttonText=unicode(buttonText,"utf-8")




    tas = textgen.TextAutoSize(buttonText,IMAGE_WIDTH,IMAGE_HEIGHT,FONT_PATH, linePadding=0)
    result=tas.drawOptimalText(textOffsetPercent=0.25)


    fh=open(filePath,'w')
    result.save(fh, "PNG")
    fh.close()

    #print filePath
