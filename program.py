""" Unsupervised variable subset selection methods for multivariate time series (MTS) based
on common principal component analysis (CPCA), named CLeVer. 

Research paper 2: Feature Subset Selection and Feature Ranking for Multivariate Time Series ( Hyunjin Yoon, Kiyoung Yang, and Cyrus Shahabi )"""


import argparse
import os
import cv2
import numpy as np
from scipy.linalg import svd

def get_bands(images_path):
    files= sorted(os.listdir(images_path))
    print("Number of images is :", len(files))
    loading = []
    threshold = 10
    pi = []
    for indx, file_name in enumerate(files):
        img = cv2.imread(images_path+file_name) 
        print(images_path+file_name)
        img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        U, s, VT = svd(np.corrcoef(img_gray))
        loading.append(U)
        varience = np.var(s)
        percentVar = 100*(varience/(np.sum(s)))
        if (percentVar >= threshold ):
            pi.append(int(percentVar))
            print("The variance of "+file_name[:-3]+" :", int(percentVar))
    p = np.amax(pi)
    Z = [x for _,x in sorted(zip(pi,files))]
    print(Z)  
        

def get_cmd_args():

    parser = argparse.ArgumentParser()
    parser.add_argument("images", type=str, help='Images directory path')
    return parser.parse_args()



if __name__ == "__main__":
    args = get_cmd_args()
    get_bands(args.images)