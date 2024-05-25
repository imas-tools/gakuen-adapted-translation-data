import os,json
import posixpath
from imas_tools.story.story_csv import StoryCsv

data_dir = "./data"

if __name__ == "__main__":
    index = {}
    for subdir, _, files in os.walk(data_dir):
        for file in files:
            if not file.endswith(".csv"):
                continue
            file_path = posixpath.join(subdir, file)
            with open(file_path, "r", encoding="utf-8") as f:
                # print(file_path)
                # print(f.readlines())
                story_csv = StoryCsv("".join(f.readlines()))
                index[story_csv.origin] = file_path

    with open("./index.json", "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=4)
