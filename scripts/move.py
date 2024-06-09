import os
import json
import shutil
from imas_tools.story.story_csv import StoryCsv


def read_index(index_path="./index.json") -> dict[str, str]:
    with open(index_path, "r", encoding="utf-8") as file:
        return json.load(file)

# supposed to return ***.txt
def read_original_name(sub_dir, file_path):
    with open(os.path.join(sub_dir, file_path), 'r', encoding='utf-8') as file:
        story = StoryCsv(file.readlines())
        return story.origin

def move_csv_files(root_dir, dest_dir=None):
    print("moving")
    print("root dir:", root_dir)
    print("dest dir:", dest_dir)
    index = read_index()
    if dest_dir is None:
        dest_dir = root_dir
    # 遍历根目录及其子目录下的所有文件
    errors = []
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            try:
                if file.endswith(".csv"):
                    # 去掉文件扩展名
                    original_name = read_original_name(subdir, file)
                    if original_name in index:
                        raise ValueError(f"File already in data: {original_name}")
                    file_name = os.path.splitext(original_name)[0]
                    # 使用下划线分隔文件名，创建新目录结构
                    new_path = os.path.join(dest_dir, *file_name.split('_')) + ".csv"
                    print(f"Moving file to {new_path}")
                    new_dir = os.path.dirname(new_path)
                    # 创建新目录
                    os.makedirs(new_dir, exist_ok=True)
                    # 移动文件
                    shutil.move(os.path.join(subdir, file), new_path)
            except ValueError as e:
                errors.append(e)
    if len(errors) > 0:
        raise Exception(errors)

# 示例调用
root_directory = "./tmp"
dest_directory = "./data"
move_csv_files(root_directory, dest_directory)
