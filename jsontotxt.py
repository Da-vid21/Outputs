#!/bin/env python3
import ann
import pandas as pd
from json2py import *

with open("/home/dawit/IaaAgDataNER/Data/UIdaho2019/small_grains_report_2019_p41_td.json") as f:
    data = json.load(f)
   data= data.values()
File_object = open(r"output.txt", "r+")
Str = ' '.join(map(str, data))
File_object.write(Str)
