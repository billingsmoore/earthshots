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
for i in range(1): # just test on one coordinate
    # get coordinate from list
    coord = coords[i][0].replace(' ', '')
    
    # screenshot of coordinate from straight above
    url = 'https://earth.google.com/web/@' + coord + ',143000d'
    driver.get(url)
    time.sleep(5)
    driver.save_screenshot('../earthshots-data/pics/' + coord.replace(',', '-') + '.png')

    url_30 = url + ',30r'