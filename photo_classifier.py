from os import makedirs, path, walk
from shutil import move
from argparse import ArgumentParser
from exifread import process_file


def getFlist(file_dir):
    file_list = []
    for root, dirs, files in walk(file_dir):
        print('root_dir:', root)  # 当前路径
        print('sub_dirs:', dirs)  # 子文件夹
        print('files:', files)  # 文件名称，返回list类型
        file_list.append(files)
    return file_list


def makedir(dir_path):
    if path.exists(dir_path):
        return None
    makedirs(r"" + dir_path)


def get_exif_date(file):
    with open(path.join(file_dir, file), "rb") as file_data:
        tags = process_file(file_data)
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
    parser = ArgumentParser()
    parser.add_argument('--file_dir', default='D:\\照片', type=str, required=True,
                        help='The directory of photos. For example: "D:\\照片\\5月".')
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
        dst = path.join(file_dir, dir_name)
        makedir(dst)

        print(path.join(file_dir, file))

        try:
            move(path.join(file_dir, file), dst)
        except Exception as e:
            print(e)
            continue
