import cv2 
import numpy as np

if __name__ == "__main__":
    img = cv2.imread('./dataset/photo.jpg',  
                    cv2.IMREAD_GRAYSCALE) 
    
    cv2.imshow('image', img) 
    cv2.waitKey(0) 
    cv2.destoryAllWindows() 