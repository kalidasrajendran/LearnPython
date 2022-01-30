import sys
import os
from PIL import Image, ImageFilter


# run command line
# jpg_to_png_converter.py D:\1_Learning\C_C++\Repo\2021_10_18\LearnCPlusPlus\Python\scripting\pics D:\1_Learning\C_C++\Repo\2021_10_18\LearnCPlusPlus\Python\scripting\png_pics

# grab 
src_folder = sys.argv[1]
output_folder = sys.argv[2]

print('source folder: ', src_folder)
print('output folder: ', output_folder)

# create output folder
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

if os.path.exists(src_folder):
    for file in os.listdir(src_folder):        
        fileext = os.path.splitext(file)[1]
        if fileext == '.jpg':
            imgpath = os.path.join(src_folder, file)
            src_image = Image.open(imgpath)

            # create output file name
            outfilename = os.path.join(output_folder, file)
            pre = os.path.splitext(outfilename)[0]
            outfilename = pre + '.png'
            print(outfilename)

            # save file
            src_image.save(outfilename, 'png')
else:
    print('source folder not found: ', src_folder)