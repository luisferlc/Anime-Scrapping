# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 12:57:05 2020

@author: luisf
"""

import requests
from bs4 import BeautifulSoup as bs
import time
import pandas as pd


response=requests.get('https://myanimelist.net/anime/38329/Seishun_Buta_Yarou_wa_Yumemiru_Shoujo_no_Yume_wo_Minai', verify=False)
res_text = response.text
soupa = bs(res_text, 'html.parser')
soupa
##################
#Title:
title_string = soupa.select('h1 span')
title_string
title_string=str(title_string)
title_string
time.sleep(2) #Me has salvado la vida
title_string=title_string.split(">")
print(title_string)
title_string=title_string[2].replace("</span", "")
print(title_string)
###############################################################################
#airing
soupa_varios=soupa.findAll('div', {'class' :'spaceit'})
aired=str(soupa_varios[1])
aired
aired=aired.split("\n ")
aired[1]


if 'to' in aired[1]:
    print("YES")
    aired=aired[1].split("to")
    start_airing=aired[0].strip()
    end_airing=aired[1].strip()
else:
    start_airing= aired[1].strip()
    end_airing='-'
    
    
######################################################################################
    
from web_project_anime import  *

url_pattern = 'https://myanimelist.net/topanime.php?limit=%s.html'

for i in range(0, 100,50):
    print(url_pattern % i)

##############
# Starting Season
typo = soupa.select('span + a')
typo = typo[0]
typo =str(typo)
typo =typo.split(">")
typo = typo[1].replace("</a", "")
print(typo)

if typo == 'TV':
    sseason=soupa.find("span", text="Premiered:").nextSibling.nextSibling
    #print(sseason)
    #if '>' in sseason:
    sseason=str(sseason).split(">")[1].split(" ")[0]
    print(sseason)
else:
    sseason = '-'
    print(sseason)
    