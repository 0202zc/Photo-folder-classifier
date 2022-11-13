import os
import shutil
import argparse


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


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_dir', default='D:\\photos', type=str, required=True, help='The directory of photos. For example: "D:\\photos\\11".')
    parser.add_argument('--type', default='realme', type=str, required=False, help='The type of camera, such as "xiaomi" and "realme". To identify the patten of filename.')
    args = parser.parse_args()

    type = args.type
    file_dir = args.file_dir
    file_name = getFlist(file_dir)[0]

    for file in file_name:
        if type == 'xiaomi':
            date = file.split('_')[1]
            month = int(date[4:6])
            day = int(date[6:8])
        if type == 'realme':
            print(file)
            date = file.split('_')[1] if file.__contains__('IMG_') else file[3:11]
            month = int(date[4:6])
            day = int(date[6:])

        dir_name = str(month) + "." + str(day)
        dst = os.path.join(file_dir, dir_name)
        makedir(dst)

        print(os.path.join(file_dir, file))

        try:
            shutil.move(os.path.join(file_dir, file), dst)
        except Exception as e:
            print(e)
            continue
