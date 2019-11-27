# Yandere Pool Downloader

## Introduction
Yandere Pool Downloader is a simple command line program to download images from the [Yande.re website](https://yande.re) by pool numbe. The program is written in Python 3.

## Setting Up
1. Download and install the latest version of [Python](https://www.python.org/downloads/)
2. Open the Command Prompt (for Windows) or Terminal (for MacOS).
3. Run the following commands:
```
pip install requests
pip install argparse
```

## Running the Program
1. Using the Command Prompt, change to the directory to where the file `yandere_pool_downloader.py` is located. E.g. `cd D:\yandere_pool_downloader`
2. Run the following command: `python yandere_pool_downloader.py <Pool No.> <sample/full>`
   1. Pool No. - the pool number
   2. sample/full - Specify `sample` or `full`. Choosing `sample` will download a smaller version of the image, while `full` is the full version
   3. Example: `python yandere_pool_downloader.py 96832 full` or `python yandere_pool_downloader.py 96832 sample`
3. The image will be saved in the folder `yandere/<Pool No.>_<Pool Name>`:
![image001.png](/images/img001.png)
