import cv2
import numpy as np
import os

folders = ["airplane", "car", "cat", "dog", "flower", "fruit", "motorbike", "person"]

path = "Image Compression/training data/images/data/natural_images/"

for folder in folders:
    for filename in os.listdir(path + folder):
        file_path = path + folder + "/" + filename
        print(filename)
        
        img = cv2.imread(file_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow(folder + "/" + filename, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        img_array = np.array(img)
        img_list = img_array.tolist()
        oldimg = img_list
    
        for i in range(1, len(img_list), 2):
            img_list[i] = [0] * len(img_list[i])

        
        with open('Image Compression/training data/trainingdata.csv', 'a') as f:
            for i in range(1,len(img_list)-1, 2):
                for j in range(len(img_list[i])):
                    print(oldimg[i-1][j],oldimg[i][j],oldimg[i+1][j], img_list[i-1][j],img_list[i][j],img_list[i+1][j])
                    #f.write(str(img_list) + '\n')
        

        # img_list = np.array(img_list)
        # img_list = img_list.astype(np.uint8)

        # cv2.imshow("original.jpg", img_list)
        # cv2.imwrite("Image Compression/compressed.png", img_list)

        # cv2.waitKey(0)