from argparse import ArgumentParser
from exifread import process_file
from os import makedirs, walk
from os.path import exists, join
from shutil import move


def getFlist(file_dir):
    file_list = []
    for root, dirs, files in walk(file_dir):
        print('root_dir:', root)  # current directory
        print('sub_dirs:', dirs)  # subdirectory
        print('files:', files)  # file name -> list
        file_list.append(files)
    return file_list


def makedir(dir_path):
    if exists(dir_path):
        return None
    makedirs(r"" + dir_path)


def get_exif_date(file):
    with open(join(file_dir, file), "rb") as file_data:
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


def get_date_by_filename(file):
    date = file.split("_")[1]
    month, day = int(date[4:6]), int(res[-2:])
    return month, day


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--file_dir', default='D:\\照片', type=str, required=True,
                        help='The directory of photos. For example: "D:\\照片\\1月".')
    args = parser.parse_args()

    file_dir = args.file_dir
    if not exists(file_dir):
        print('The directory of photos is not exist.')
        exit(-1)
    file_name = getFlist(file_dir)[0]

    for file in file_name:
        # The video has no EXIF, using filename to get the date.
        if file.endswith('.mp4'):
            res = str(file).split('.')[0].split('_')[1]
            month, day = int(res[4:6]), int(res[-2:])
        else:
            res = get_exif_date(file)
            if res is None:
                # If there is no EXIF, using file name to get the date.
                res = get_date_by_filename(file)
                if res is None:
                    exit(-1)
            month, day = res

        dir_name = str(month) + "." + str(day)
        dst = join(file_dir, dir_name)
        makedir(dst)

        print(join(file_dir, file))

        try:
            move(join(file_dir, file), dst)
        except Exception as e:
            print(e)
            continue
