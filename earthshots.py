from selenium import webdriver
import time
import csv

# read in coordinates as list
file = open("earthshots-data/coordinates.csv", "r")
coords = list(csv.reader(file, delimiter=","))
file.close()

# initialize driver
driver = webdriver.Chrome()

# iterate over coordinates and take screenshots
for i in range(len(coords)//2):
    
    coord = coords[i][0].replace(' ', '')
    
    url = 'https://earth.google.com/web/@' + coord + ',143000d'
    
    driver.get(url)
    time.sleep(10)

    driver.save_screenshot('pics/' + coord.replace(',', '-') + '.png')