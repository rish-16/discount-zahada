import wget, os, re
from bs4 import BeautifulSoup    

PATH = "../../pages/"
pages_dir = os.listdir(PATH)

def get_image_names(path):
    image_names = None
    with open(path, 'r') as f:
        content = f.read().strip()
        
        soup = BeautifulSoup(content, "html.parser")
        elements = soup.find_all('img')
        
        if len(elements) > 0:
            image_names = list(map(lambda el : el['src'], elements))
        
    return image_names

all_images = []
for page_path in pages_dir:
    names = get_image_names(PATH + page_path)
    if names != None:
        all_images.extend(names)
    
all_images = list(set(all_images))

# download all images
def download(name):
    img_url = f'http://mcgov.co.uk/riddles/images/{name}'
    wget.download(img_url)
    
for img in all_images:
    download(img)