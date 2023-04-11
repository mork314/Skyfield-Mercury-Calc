from skyfield.api import load
import pandas as pd
import os
import numpy as np

planets = load('de421.bsp')
earth, planet = planets['earth'], planets['mercury']
ts = load.timescale()
position_list = []
date_list = []


for i in range(150):
    year =  1900 + i
    for i in range(1, 13):
        month = i
        
        for i in range(1, 29):
            day = i
            date_list.append(f'{year} {month} {day}')
            time = ts.tt(year, month, day, 12, 0)
            position = earth.at(time).observe(planet)
            ra, dec, distance = position.radec()
            position_list.append(distance)
    
mercury_dict = {'dates':date_list, 'distances':position_list}
df = pd.DataFrame(mercury_dict)
#os.makedirs('D:/fortnitehamburger', exist_ok=True)
df.to_csv('D:/mercury.csv')

x_values = date_list
y_values = position_list

def objective(x, a, b, c):
    return a * x + b

