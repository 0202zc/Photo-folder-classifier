# Photo-folder-classifier
Create folders by date based on the default file name of the photo.

<br>

For example:

```sh
D:\\photos\\11\\IMG20221104113200.jpg -> D:\\photos\\11\\11.4\\IMG20221104113200.jpg
```



## Requirements

- Python 3.8+
- Windows 10+

## Run

run `photo_classifier.bat` after modifying the file path `--file_dir`

<br>OR

<br>

Execute the following command in cmd:

```sh
python photo_classifier.py --file_dir="YOUR FILE DIRECTORY" --type="CHOOSE ONE OF THE TYPE: [xiaomi, realme]"
```


## UPDATE
- 2024-07-07: Read EXIF data to classify photos.