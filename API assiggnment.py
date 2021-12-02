#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 11:30:10 2021

@author: samanthabenjamin
"""

!pip install requests

import requests
import pandas as pd

## This api explains the latest number of confirmed cases, recoveries and deaths 
#from a public Google Sheet published by the team at the Center for Systems Science and 
#Engineering (CSSE) at John Hopkins University

#Connecting to the api
#pull data and added dataframes
covidresponsejson = requests.get('https://coronavirus.m.pipedream.net/')
covidresponsejson.json()
covidresponse = covidresponsejson.json()


covidresponse_Rawdata = covidresponse ['rawData']
covidresponse_Rawdatadf = pd.DataFrame(covidresponse_Rawdata)

covidsimple = pd.DataFrame(covidresponse ['rawData'])
