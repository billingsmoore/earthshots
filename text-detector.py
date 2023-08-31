import pytesseract
import os
from PIL import Image

def detect_captions(dir):
    counter = 0
    i = 0
    total = len(os.listdir(dir))
    lst = [] 
    error_count = 0

    # make new directory for images
    try:
        os.makedirs(dir + '/text-found')
    except:
        print('error making directory for images with text')

    # for each image in the folder, detect the text with psm setting 6. 
    # if text is detected, delete the image
    for file in os.listdir(dir):
        i +=1
        # read the image
        try:
            orig_img = Image.open(dir + '/' + file)

            # preprocess image
            img = orig_img.point(lambda i: (i-220)*50)

            # img.save('out/' + file)

            # detect the text with
            text = pytesseract.image_to_string(img, config='--psm 4')

            text = text.strip().replace('\n', '').replace(' ', '').replace('\x0c', '')

            # if text is detected, delete the image
            if text != '':
                #print(text)
                lst.append(str(text))
                counter += 1
                # delete image
                orig_img.save(dir + '/text-found/' + file)
                os.remove(dir + '/' + file)
                print(file + ' deleted')

            # print progress

            # clear previous progress
            os.system('clear')
            # progress bar
            length = 50
            progress = int(round((i / total) * length, 0))
            filled = '█' * progress
            not_filled = '-' * (length - progress)
            bar = '[' + filled + not_filled + ']'

            # print current progress
            print('Program Running...')
            print(bar)
            print(str(i) + '/' + str(total) + ' files checked')
            print(str(counter) + ' images with text found so far')
            print(str(error_count) + ' errors opening images')

        except:
            print('error opening file ' + str(i))
            error_count += 1

    # print results
    print('Final Results:')
    print(str(total) + ' images processed')
    print(str(counter) + ' images with text found')
    print(str(error_count) + ' errors opening images')

detect_captions('../earthshots-data/model-datasets/train/no_runways (copy)')