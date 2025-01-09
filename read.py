from PIL import Image
import cv2
import pytesseract
from textblob import TextBlob
import webp
import os
import shutil
dest="/Users/akshsinha/Desktop/two-way-sign-language-translator-master/gif_data/"
op_dest="/Users/akshsinha/Desktop/two-way-sign-language-translator-master/filtered_data"
for i in range(107): #filters .webp files, extracts the text from the first frame of the files and renames them with the extracted text
    ip=dest+str(i)+".webp"
    op=dest+"tmp.gif"
    anim = webp.load_images(ip)
    anim[0].save(op, save_all=True, append_images=anim[0:1], duration=1, loop=0)
    im = Image.open(op)
    im.seek(0)
    im.save("tmp.png")
    img=cv2.imread("tmp.png")
    try:
        crop_img = img[0:170,200:470]
        txt = pytesseract.image_to_string(crop_img) #extracts the text from the first frame
    except:
        txt=""
    word=txt.replace("\n", "")
    word=word.replace(" ", "")
    word = ''.join(filter(str.isalnum, word))
    word=word.lower()
    b = TextBlob(word) #corrects the spellings
    ans=str(b.correct())
    print("corrected text: "+ans)
    if(len(ans)>0):
        fname=op_dest+ans+".webp"
        shutil.copyfile(ip, fname) #renames the files
    else:
        fname=op_dest+"unknown"+str(i)+".webp"
        shutil.copyfile(ip, fname)

