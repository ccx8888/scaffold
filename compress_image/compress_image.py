import os
from PIL import Image

# 设置工作目录并检查
os.chdir('D:/桌面/zip_image')
print("当前工作目录:", os.getcwd())  # 打印当前工作目录

def compress_image(input_image_path, output_image_path, quality=85):
    try:
        # 打开图片
        with Image.open(input_image_path) as img:
            # 获取图片格式
            img_format = img.format
            print(f"图片格式: {img_format}")  # 输出图片格式
            
            # 压缩并保存图片
            img.save(output_image_path, format=img_format, quality=quality, optimize=True)

        print(f"图片已压缩并保存到: {output_image_path}")
    except Exception as e:
        print(f"处理图片时出错: {e}")

# 示例用法
input_image = './xiangma-logo.png'  # 输入图片路径
output_image = './compressed_image.png'  # 输出图片路径
compress_image(input_image, output_image, quality=70)  # 调整质量（70表示压缩较高）
