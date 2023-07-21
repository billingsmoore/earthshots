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

# function to take pics
def take_pics(coord):   
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

# read in coordinates as list
file = open("../earthshots-data/coordinates.csv", "r")
coords = list(csv.reader(file, delimiter=","))
file.close()

# initialize driver
driver = webdriver.Chrome()

# iterate over coordinates and take screenshots
for i in range(0,len(coords)): 
    # get coordinate from list
    coord = coords[i][0].split()
    x_coord = float(coord[0].replace(',', ''))
    y_coord = float(coord[1])

    #add to coordinate to get surroundings
    displacement = .2

    west = str(x_coord+displacement) + ',' + str(y_coord)
    east = str(x_coord-displacement) + ',' + str(y_coord)
    north = str(x_coord) + ',' + str(y_coord+displacement)
    south = str(x_coord) + ',' + str(y_coord+displacement)

    surroundings = [west, east, north, south]

    # take pics
    for location in surroundings:
        take_pics(location)

    print(str(i) + '/' + str(len(coords)) + ' coordinates finished')
