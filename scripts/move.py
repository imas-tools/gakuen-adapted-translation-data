import os
import shutil

# supposed to return ***.txt
def read_original_name(sub_dir, file_path):
    with open(os.path.join(sub_dir, file_path), 'r', encoding='utf-8') as file:
        for line in file:
            if line.startswith('info'):
                return line.split(',')[1].strip()
    raise ValueError("Original name not found")

def move_csv_files(root_dir, dest_dir=None):
    print("moving")
    print("root dir:", root_dir)
    print("dest dir:", dest_dir)
    if dest_dir is None:
        dest_dir = root_dir
    # 遍历根目录及其子目录下的所有文件
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            print("file found: ", file)
            if file.endswith(".csv"):
                # 去掉文件扩展名
                file_name = os.path.splitext(read_original_name(subdir, file))[0]
                # 使用下划线分隔文件名，创建新目录结构
                new_path = os.path.join(dest_dir, *file_name.split('_')) + ".csv"
                print(new_path)
                new_dir = os.path.dirname(new_path)
                # 创建新目录
                os.makedirs(new_dir, exist_ok=True)
                # 移动文件
                shutil.move(os.path.join(subdir, file), new_path)

# 示例调用
root_directory = "./tmp"
dest_directory = "./data"
move_csv_files(root_directory, dest_directory)
