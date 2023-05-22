import streamlit as st
import pandas as pd
import numpy as np
import pickle
import base64
import chapter3 as c3
from PIL import Image
import cv2 as cv2

st.set_page_config(
    page_title="Image Processing",
    page_icon="👈",
)

app_mode = st.sidebar.selectbox('Image Processing', ['Negative', 'Logarit', 'Power', 'PiecewiseLinear',
                                'LocalHist', 'HistStat', 'BoxFilter', 'Threshold', 'MedianFillter'])


def set_bg_hack(main_bg):
    '''
    A function to unpack an image from root folder and set as bg.

    Returns
    -------
    The background.
    '''
    # set bg name
    main_bg_ext = "png"

    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )

page_bg_img = '''
    <style>
    .stApp {
        background: url("https://img.freepik.com/free-vector/hand-painted-watercolor-pastel-sky-background_23-2148902771.jpg");
        background-size: cover;
    }
    </style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)
# set_bg_hack('Image/background2.png')


def OnNegative():
    path = 'Image/Negative.tif'
    imgin = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    global imgout
    imgout = c3.Negative(imgin)
    Layout(imgin, imgout)


def OnLogarit():
    path = 'Image/Logarit.tif'
    imgin = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    global imgout
    imgout = c3.Logarit(imgin)
    Layout(imgin, imgout)


def OnPower():
    path = 'Image/Power.tif'
    imgin = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    global imgout
    imgout = c3.Power(imgin)
    Layout(imgin, imgout)


def OnPiecewiseLinear():
    path = 'Image/PiecewiseLinear.tif'
    imgin = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    global imgout
    imgout = c3.PiecewiseLinear(imgin)
    Layout(imgin, imgout)


def OnLocalHist():
    path = 'Image/LocalHist.tif'
    imgin = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    global imgout
    imgout = c3.LocalHist(imgin)
    Layout(imgin, imgout)


def OnHistStat():
    path = 'Image/LocalHist.tif'
    imgin = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    global imgout
    imgout = c3.HistStat(imgin)
    Layout(imgin, imgout)


def OnBoxFilter():
    path = 'Image/BoxFilter.tif'
    imgin = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    global imgout
    imgout = c3.BoxFilter(imgin)
    Layout(imgin, imgout)


def OnThreshold():
    path = 'Image/Threshold.tif'
    imgin = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    global imgout
    imgout = c3.Threshold(imgin)
    Layout(imgin, imgout)


def OnMedianFillter():
    path = 'Image/MedianFillter.tif'
    imgin = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    global imgout
    imgout = cv2.medianBlur(imgin, 7)
    Layout(imgin, imgout)


def Layout(imgin, imgout):
    col1, col2 = st.columns(2)
    col1.header(':red[Before]')
    col1.image(imgin, use_column_width=True)
    col2.header(':green[After]')
    col2.image(imgout, use_column_width=True)


if app_mode == 'Negative':
    st.subheader(':violet[Negative]')
    OnNegative()
elif app_mode == 'Logarit':
    st.subheader(':violet[Logarit]')
    OnLogarit()
elif app_mode == 'Power':
    st.subheader(':violet[Power]')
    OnPower()
elif app_mode == 'PiecewiseLinear':
    st.subheader(':violet[PiecewiseLinear]')
    OnPiecewiseLinear()
elif app_mode == 'LocalHist':
    st.subheader(':violet[LocalHist]')
    OnLocalHist()
elif app_mode == 'HistStat':
    st.subheader(':violet[HistStat]')
    OnHistStat()
elif app_mode == 'BoxFilter':
    st.subheader(':violet[BoxFilter]')
    OnBoxFilter()
elif app_mode == 'Threshold':
    st.subheader(':violet[Threshold]')
    OnThreshold()
elif app_mode == 'MedianFillter':
    st.subheader(':violet[MedianFillter]')
    OnMedianFillter()