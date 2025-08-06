import cv2
import os
from skimage.metrics import peak_signal_noise_ratio
from skimage.metrics import structural_similarity as compare_ssim


def calculate_metrics(folder1, folder2):
    
    files1 = os.listdir(folder1)
    files2 = os.listdir(folder2)
    
    
    total_psnr = 0
    total_ssim = 0
    
    for file1, file2 in zip(files1, files2):
        
        img1 = cv2.imread(os.path.join(folder1, file1))
        img2 = cv2.imread(os.path.join(folder2, file2))
        
        
        psnr = peak_signal_noise_ratio(img1, img2)
        ssim = compare_ssim(img1, img2, channel_axis=2)
        
        
        total_psnr += psnr
        total_ssim += ssim
    
    
    num_images = len(files1)
    avg_psnr = total_psnr / num_images
    avg_ssim = total_ssim / num_imagesVIF
    
    return avg_psnr, avg_ssim


folder1 = '/home/u2308283087/YQ/newModel1/test_resultsDL1DH2/SrFFHQ'
folder2 = 'HighTest_BI'
avg_psnr, avg_ssim = calculate_metrics(folder1, folder2)

print('平均 PSNR: ', avg_psnr)
print('平均 SSIM: ', avg_ssim)
