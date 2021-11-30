from numpy import int0
import pandas as pd 
import csv 

df = pd.read_csv('C:/Users/aadi_/Desktop/projects/calculating-garvity/final_data.csv')

radius = df['Radius'].to_list()
mass = df['Mass'].to_list()




gravity = []

for i in range(0,len(radius)-1):
    
    radius[i] = radius[i]*6.957e+8
    mass[i] = mass[i]*1.989e+30

def gravity_cal(mass,radius):
    G = 6.674e-11
    for index in range(0,len(mass)):
        g = (mass[index]*G)/((radius[index])*2)
        gravity.append(g)

gravity_cal(mass,radius)

df['gravity'] = gravity
print(df)

df.to_csv('final.csv')