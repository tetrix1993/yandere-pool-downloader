import urllib.request
import argparse
from myutil.util import create_directory
from myutil.util import download_image
from myutil.util import get_response
from myutil.util import get_response_with_header
from myutil.util import is_file_exists

parser = argparse.ArgumentParser()
parser.add_argument('P', help = 'Pool ID')
parser.add_argument('T', help = 'Type - full or sample')
args = parser.parse_args()

BASE_FOLDER = "yandere"
POOL_LINK = "https://yande.re/pool/show/" + args.P
IMAGE_PAGE_LINK_PREFIX = "https://yande.re/post/show/"

def get_pool_title(text):
    text = text.split('<div id="pool-show">')[1].split('</h4>')[0].split('<h4>Pool: ')[1]
    text = text.replace('<','').replace('>','').replace(':','').replace('"',"'") \
        .replace('/','').replace('\\','').replace('|','').replace('?','').replace('*','') \
        .replace(' ', '_')
    return text

def process_pool_page(url):
    if not('full' in args.T or 'sample' in args.T):
        print("Indicate 'full' or 'sample'")
        return
    response = get_response_with_header(POOL_LINK)
    if (len(response) != 0):
        save_folder = BASE_FOLDER + "/" + args.P + '_' + get_pool_title(response)
        create_directory(save_folder)
        first_split = response.split("<div id=\"pool-show\">")[1]
        second_split = first_split.split("<script type=\"text/javascript\">")[0]
        third_split = second_split.split(IMAGE_PAGE_LINK_PREFIX)
        for i in range(len(third_split)):
            if i == 0:
                continue
            page_id = third_split[i].split("</span>")[0]
            process_image_page(IMAGE_PAGE_LINK_PREFIX + page_id, page_id, save_folder)

def process_image_page(url, page_id, save_folder):
    filepath = save_folder + "/" + page_id + ".jpg"
    if (is_file_exists(filepath)):
        print("File exists: " + filepath)
        return
    response = get_response(url)
    if (len(response) != 0) and "<div id=\"note-container\">" in response:
        image_url = response.split("<div id=\"note-container\">")[1] \
            .split("src=\"")[1] \
            .split("\"")[0]
        if 'full' in args.T:
            image_url = image_url.replace('sample','image')
        download_image(image_url, filepath)

process_pool_page(POOL_LINK)
        
