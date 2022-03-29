import cv2
import numpy as np
import glob
 
img_array = []
for filename in glob.glob(str(input("<exmple enter_ D://amr_1//amr_hac//*.jpg _path..:/>"))):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)#   الحاق مصفوفة (صورة) الى نهاية المصفوفة
 
 
out = cv2.VideoWriter(input("<example(video.avi)enter_name_video_:>"),cv2.VideoWriter_fourcc(*'DIVX'),2*10, size)
print ("AMR","al_mdhrhi","cv2")
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
