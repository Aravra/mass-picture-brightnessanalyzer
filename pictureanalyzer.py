import matplotlib.pyplot as plt
import os
from PIL import Image
from numpy import trapz

def calculate_brightness(image):
    greyscale_image = image.convert('L')
    histogram = greyscale_image.histogram()
    pixels = sum(histogram)
    brightness = scale = len(histogram)

    for index in range(0, scale):
        ratio = histogram[index] / pixels
        brightness += ratio * (-scale + index)

    return 1 if brightness == 255 else brightness / scale

def main():
    folder_dir = "G:/arav/sk video"
    directorylist =  os.listdir(folder_dir)
    arealist = []

    del directorylist[1:]

    #del directorylist[0]
    #del directorylist[-1]
    #del directorylist[-1]
    fig, axs = plt.subplots(5)
    for i in directorylist:
        directorylist2 = os.listdir(folder_dir+"/"+i)
        for t in directorylist2:
            pointslist = []
            for images in os.listdir(folder_dir+"/"+i+"/"+t):
                if (images.endswith(".tif")):
                    image = Image.open(folder_dir+"/"+i+"/"+t+"/"+images)
                    pointslist.append(calculate_brightness(image))
            for line in pointslist:
                #if line >0.004:
                if line >0.0025:
                    indexline = pointslist.index(line)
                    break
            indexdelete = indexline - 30
            if indexdelete <0:
                indexdelete = 0
            del pointslist[:indexdelete]
            axs[directorylist2.index(t)].set_xlim([0,600])
            #axs[directorylist2.index(t)].set_ylim([0,0.75])
            axs[directorylist2.index(t)].set_ylim([0,0.01])
            axs[directorylist2.index(t)].set_xticks([0,60,120,180,240,300,360,420,480,540],[0,1,2,3,4,5,6,7,8,9])
            axs[directorylist2.index(t)].set_xlabel("tijd(s)")
            axs[directorylist2.index(t)].set_ylabel("relatieve lichtinval")
            #concentratielist = [17.86,26.79,35.71,44.64,53.57]
            concentratielist = [250,375,500,625,750]
            #expindex = directorylist2.index(t) +6
            expindex = directorylist2.index(t) +1
            #axs[directorylist2.index(t)].set_title("exp"+str(expindex)+": concentratie NaOCl: "+str(concentratielist[directorylist2.index(t)]))
            axs[directorylist2.index(t)].set_title("exp"+str(expindex)+": concentratie H2O2: "+str(concentratielist[directorylist2.index(t)]))
            axs[directorylist2.index(t)].plot(pointslist)
            #area = trapz(pointslist)
            area = trapz(pointslist)
            arealist.append(area)
    print(*arealist)
    plt.show()
main()