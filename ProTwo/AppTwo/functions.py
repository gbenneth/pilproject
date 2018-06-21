#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 22:39:25 2018

@author: genebenneth
"""
from PIL import Image, ImageChops
import os, time


def handle_uploaded_file(file):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MASK_IMG_PTH = os.path.join(BASE_DIR,"ProTwo/static/images/Pillow_Mask.jpg")
    MAIN_IMG_PTH = os.path.join(BASE_DIR,"ProTwo/static/images/Pillow_Square_LG.jpg")
    SHAD_IMG_PTH = os.path.join(BASE_DIR,"ProTwo/static/images/Pillow_Shadow.jpg")
    TEMP_PTH = os.path.join(BASE_DIR,"ProTwo/Temp/")
    
    main = Image.open(MAIN_IMG_PTH).convert("RGB")
    srce = Image.open(file).convert("RGB").resize(main.size)
    mask = Image.open(MASK_IMG_PTH).convert("L").resize(main.size)
    
    base = Image.new("RGB",main.size)
    pillow_art = srce.resize((1821,1741))
    base.paste(pillow_art,(282,230))
    
    first_img=Image.composite(base, main, mask)
    shadow=Image.open(SHAD_IMG_PTH).convert("RGB").resize(main.size)

    Fimg = ImageChops.multiply(first_img,shadow)
    t = time.localtime()
    timestamp = time.strftime('%b%d%Y%H%M%S.jpg', t)
    Fimg_PTH = os.path.join(TEMP_PTH,timestamp)
    Fimg.save(Fimg_PTH)
    return Fimg_PTH
