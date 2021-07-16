import requests

sites = {
    'level1': 'http://www.mcgov.co.uk/riddles/level1.html',             # level 1
    'youranswer': 'http://www.mcgov.co.uk/riddles/youranswer.html',     # level 2
    'eye': 'http://www.mcgov.co.uk/riddles/eye.html',                   # level 3
    'ninety': 'http://www.mcgov.co.uk/riddles/ninety.html',             # level 4
    'luck': 'http://www.mcgov.co.uk/riddles/luck.html',                 # level 5
}

for name, url in sites.items():
    req = requests.get(url, 'html.parser')

    with open('../pages/' + name + '.html', 'w') as f:
        f.write(req.text)
        f.close()