import os


## Main function dependencies
from PIL import Image
from numpy import asarray
import cv2
import numpy as np

#################
#Main Function

def compare_pic (i1,i2):
    image1=Image.open(i1)
    image2=Image.open(i2)
    data1=asarray(image1)
    data2=asarray(image2)
    errorl2=cv2.norm(data1,data2,cv2.NORM_L2)
    similarity=1- errorl2/((image1.size[0])*(image1.size[1]))
    return(similarity)
##################

#   Factor of Determination
factor=0.945


##################

# 1 traverse all pictures into a list
def list_of_pic():
    formats = ('.jpg', '.jpeg')
    cwd = os.getcwd()
    pictures=[]
    for file in os.listdir(cwd):
        if os.path.splitext(file)[1].lower() in formats:
            path=os.path.join(cwd,file)
            pictures.append(path)
            
    return(pictures)

##################

#2 open picture 1 & compare it to the rest
def compare(list_pic):  # list containing address of pics
    for picture in list_pic:
        number=len(list_pic)
        if os.path.isfile(picture) == True:
            start=list_pic.index(picture)
            for k in range(start+1,number):
                compare_picture=list_pic[k]
                if os.path.isfile(compare_picture) ==True:
                    if (compare_pic(picture,compare_picture)) >= factor:
                        move_copy(compare_picture)
                    else:
                        pass
                else:
                    pass
        else:
            pass
            

##################

# OS function 1
#       Moves if the image is duplicate

def move_copy(image):
        cwd = os.getcwd()
        fol=os.path.join(cwd,"duplicate")
        if os.path.isdir(os.path.join(cwd,"duplicate")) == False:
            os.mkdir(fol)
        import shutil
        print("MOVING -->",image)
        shutil.move(image,fol)
        

##################

# Initiating main function
print("list_pictures")
list_pictures=list_of_pic()
compare(list_of_pic())
print("## Comparison DONE ##")
