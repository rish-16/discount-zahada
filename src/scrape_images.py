import wget, os, re, requests
from bs4 import BeautifulSoup

PATH = "../pages/"
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
    if not os.path.isdir(PATH + page_path):
        names = get_image_names(PATH + page_path)
        if names != None:
            all_images.extend(names)
    
all_images = list(set(all_images))

# download all images
def download(name):
    print (name)
    img_url = f'http://mcgov.co.uk/riddles/{name}'
    # wget.download(img_url, out=f"../pages/{name}")
    os.system(f"wget {img_url} -O ../pages/{name}")
    # with open(f'../pages/{name}', 'wb') as f:
        # f.write(requests.get(img_url).content)

for img in all_images:
    download(img)