import cv2
import os

def crop_image(image_name):

    image = cv2.imread(image_name)

    startx = 75
    endx=1365
    starty = 0
    endy=663

    crop = image[starty:endy,startx:endx]

    return crop

def process(directory, image):

    path = directory + '/' + image

    crop = crop_image(path)

    cv2.imwrite('cropped/cropped-' + image, crop)

def main():
    directory = input('Enter directory of images: ')
    for image in os.listdir(directory):
        process(directory, image)

main()