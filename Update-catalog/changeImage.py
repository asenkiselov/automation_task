#!/usr/bin/env python3
from PIL import Image
import os,sys


def main(directory):
    #new_dir = '/opt/icons/'
    for filename in os.listdir(directory):
        if filename.endswith('.tiff'):
            # print(filename)
            outfilename = filename[:-4] + "jpeg"
            img = Image.open(directory + filename)
            out = img.resize((600,400)).convert("RGBA")
            background = Image.new('RGBA', out.size, (255, 255, 255))
            final = Image.alpha_composite(background, out).convert("RGB")
            new_file = directory + outfilename
            # new_im = img.resize((128, 128))
            # new_img = img.rotate(-90)
            final.save(new_file,'JPEG', quality=80)
 #im.rotate(90).resize((192, 192)).save("/opt/icons/" + filename)



if __name__ == "__main__":
    user = os.environ.get('USER')
    directory = '/home/'+user+'/supplier-data/images/'#sys.argv[1]
    main(directory)
    sys.exit(0)

