import os
import cv2

# 定义降采样因子，这里设定为4，即将图像的大小缩小为原始大小的1/4
downscale_factor = 4

# 遍历图像文件夹中的所有文件
input_folder = ""
output_folder = ""

for filename in os.listdir(input_folder):
    # 确保文件是图像文件
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        # 构建输入和输出文件的完整路径
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # 读取高分辨率图像
        high_res_image = cv2.imread(input_path)

        # 使用区域插值方法调整图像大小，生成低分辨率图像
        low_res_image = cv2.resize(high_res_image, None, fx=1/downscale_factor, fy=1/downscale_factor, interpolation=cv2.INTER_AREA)

        # 保存生成的低分辨率图像
        cv2.imwrite(output_path, low_res_image)

        print(f"已生成对应的低分辨率图像：{output_path}")

print("所有图像处理完成。")
