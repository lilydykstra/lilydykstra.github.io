"""
Working with Data
In-Class Code - Tues, Nov 29

This code will be a template for working with single and multiple dimension (channel) data. 

1. Read a csv file
2. Take 1 column of data and use in animation (draw waveform)
3. Take 2 columns of data annd us in animation (change radius)
4. Get data from the internet (API), use data in drawing (add object, different color)

"""

import pygame
import pandas as pd, csv # for reading & writing files saved to your computer
import requests # for APIs
pygame.init

w = 600
h = 600
win = pygame.display.set_mode((w,h))

def csv2dict(filename="mockData.csv",full=False):
    '''Get data from a file'''
    if full:
        data = pd.read_csv(filename).to_dict(orient='list')
    else:
        data = pd.read_csv(filename, usecols=['sample', 'amp']).to_dict(orient='list')
    return data   

def data2csv(data,filename='test.csv'):
    '''Creates new file if there is none in folder.
    Arguments:
        data (any) - data to save. Data can be any Python variable
        file (str) - name of file. Must include .txt extensinon
        add (bool) - toggles appending to file. Seleect False to overwrite files.
    '''
    # Write the file to disk
    writer = open(filename, "w") # make writer object
    if type(data) in [list,tuple]:
        for row in data:
            writer.write(str(row)+" ")
    elif type(data) ==dict:
        pd.DataFrame.from_dict(data).to_csv(filename, index = False, header=True)
    else:
        writer.write(str(data))
    writer.close()
    print('File saved.')

class DataCircle:
    def __init__(self, x=w/2, y=h/2, rad=150):
        self.x = x
        self.y = y
        self.rad = rad
        self.color = [67,188,142]
        self.box = pygame.draw.circle(win,self.color,(self.x,self.y),self.rad)
        
        self.draw = True
        self.pts=[]
        
        # data attributes
        self.data = csv2dict() # get data from csv file
        self.amp = self.data['amp']
        self.idx = 0 # to step through values
        
    def show(self):
        self.box = pygame.draw.circle(win,self.color,(self.box.centerx,self.box.centery),self.rad)
        
    def changeColor(self,value, ch=0):
        '''reassigns color to value (int) based on channel: 
            r (0), g (1), b (2) or all (-1).'''
        if ch == -1:
            '''change all'''
            for ch in self.color:
                if 0<=self.color[ch]<255:
                    self.color[ch] = value
        else:
            if 0<self.color[ch]<255:
                self.color[ch] = value
                
    def move(self, dx,dy):
        '''moves circle based on Rect'''
        self.box = self.box.move(dx,dy)

    def changeRad(self,value):
        self.rad = value

    # def getAPIdata(self):
    #     URL = 'https://api.weather.gov/gridpoints/BOU/53,74/forecast'
    #     # /gridpoints/{wfo}/{x},{y}/forecast
    #     response = requests.get(URL)
    #     self.data = response.json()
    #     self.periods = self.data['properties']['periods'] # list of data by time period
    #     self.temp = self.data['properties']['periods'][0]['temperature'] # single temp measure for current time period

class Manager:
    def __init__(self):
        self.dv = DataCircle()

    def main(self):        
        #cycle through values
        idx = 0
        running = True
        
        while running:
            win.fill((0,0,0))
            
            # use mock amp data

            self.dv.changeRad(self.dv.amp[idx])
            if idx<len(self.dv.amp)-1:
                idx += 1
            self.dv.show()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     self.dv.changeColor(255)

            pygame.display.update()
            
Manager().main()