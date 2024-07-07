import os
import shutil
import argparse
import exifread


def getFlist(file_dir):
    file_list = []
    for root, dirs, files in os.walk(file_dir):
        print('root_dir:', root)  # 当前路径
        print('sub_dirs:', dirs)  # 子文件夹
        print('files:', files)  # 文件名称，返回list类型
        file_list.append(files)
    return file_list


def makedir(dir_path):
    if os.path.exists(dir_path):
        return None
    os.makedirs(r"" + dir_path)


def get_exif_date(file):
    with open(os.path.join(file_dir, file), "rb") as file_data:
        tags = exifread.process_file(file_data)
        tag_date = 'EXIF DateTimeOriginal'
        if tag_date not in tags:
            print('Cannot find "EXIF DateTimeOriginal" tag.')
            return None

        shot_date, _ = tags[tag_date].printable.split(" ")
        year, month, day = shot_date.split(":")
        month = int(month)
        day = int(day)
        return month, day


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_dir', default='D:\\照片', type=str, required=False,
                        help='The directory of photos. For example: "D:\\照片\\5月".')
    parser.add_argument('--type', default='realme', type=str, required=False,
                        help='The type of camera, such as "xiaomi" and "realme". To identify the patten of filename.')
    args = parser.parse_args()

    type = args.type
    file_dir = args.file_dir
    file_name = getFlist(file_dir)[0]

    for file in file_name:
        res = get_exif_date(file)
        if res is None:
            exit(-1)
        month, day = res

        dir_name = str(month) + "." + str(day)
        dst = os.path.join(file_dir, dir_name)
        makedir(dst)

        print(os.path.join(file_dir, file))

        try:
            shutil.move(os.path.join(file_dir, file), dst)
        except Exception as e:
            print(e)
            continue
