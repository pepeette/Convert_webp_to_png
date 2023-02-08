#pip install webptools
from webptools import dwebp
import os, glob
os.chdir("./Product Group images")

webp_list = glob.glob("*.webp")

for filename in webp_list:
    #print(filename[:-4]+"png")
    outname = (filename[:-4]+"png")
    dwebp(input_image=filename, output_image=outname, option="-o", logging="-v")
