from selenium import webdriver
import time
import csv

# google earth uses url's in the format:
# earth.google.com/web/@x,y,d,t,r
# x is latitude, y is longitude
# d is distance from the ground in meters
# t and r are rotations around separate axes
# all but x and y must contain the letter as a suffix on the numerical argument

# time to sleep to let google earth load before taking a screenshot
sleep = 10

# read in coordinates as list
file = open("../earthshots-data/2nd Russian Airbase Coordinates - Sheet1.csv", "r")
coords = list(csv.reader(file, delimiter=","))
file.close()

# initialize driver
driver = webdriver.Chrome()

total = len(coords)

# iterate over coordinates and take screenshots
for i in range(total): 
    # get coordinate from list
    coord = coords[i][0].replace(' ', '')
    
    # screenshot of coordinate from straight above
    url = 'https://earth.google.com/web/@' + coord + ',60000d'
    driver.get(url)
    time.sleep(sleep)

    # rotate t values
    for j in range(0, 61, 15):

        this_url = url +',' + str(j) + 't'

        # rotate r values
        for k in range(0, 271, 90):

            newrl = this_url + ',' + str(k) + 'r'
            driver.get(newrl)
            time.sleep(sleep)

            driver.save_screenshot('../earthshots-data/pics/' + coord.replace(',', '-') + str(j) + '-' + str(k) + '.png')

    print(str(i) + '/' + str(total) + ' coordinates done')

print('Done!')