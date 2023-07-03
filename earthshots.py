from selenium import webdriver
import time
import csv

# time to sleep to let google earth load before taking a screenshot
sleep = 10

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
    time.sleep(sleep)
    driver.save_screenshot('../earthshots-data/pics/' + coord.replace(',', '-') + '.png')

    # rotate around normal to Earth
    for j in range(90, 271, 90):

        this_url = url + +',' + str(j) + 'r'

        # screenshots from other angles
        for k in range(30, 61, 15):
            # screenshot from j degress
            newrl = url + ',' + str(k) + 't'
            driver.get(newrl)
            time.sleep(sleep)