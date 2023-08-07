# this script splits the images into tiles

import os
from PIL import Image

# define tile size
tile_size = 224

def tile(directory, filename):
# get image and dimensions
    im = Image.open(directory + '/' + filename)
    width, height = im.size

    # determine limiting dimension
    if width // tile_size <= height // tile_size:
        limiting_dimension = height
    else:
        limiting_dimension = width

    #determine how many tiles you can get
    num_tiles = limiting_dimension // tile_size

    pad_width = (width % tile_size) // 2
    pad_height = (height % tile_size) // 2

    tiles = []

    for i in range(width // tile_size):

        left = pad_width + tile_size*i
        right = left + tile_size

        for j in range(height// tile_size):

            top = pad_height + tile_size*j
            bottom = top + tile_size

            tile = (left, top, right, bottom)

            tiles.append(tile)

    tile_counter = 0

    for tile in tiles:
        im.crop(tile).save('tiled/' + filename.replace('cropped', 'tiled')[:-4] + '_' +str(tile_counter) + '.png')
        tile_counter += 1

def main():
    directory = input('Enter directory of images: ')
    counter = 0
    total = str(len(os.listdir(directory)))
    for filename in os.listdir(directory):
        tile(directory, filename)
        print(str(counter) + '/' + total + ' tiled')
        counter += 1

main()
