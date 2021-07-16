import requests

with open('answers.txt', 'r') as f:
    sites = f.read().strip().split("\n")
    
print (sites)    

for name in sites:
    url = f'http://www.mcgov.co.uk/riddles/{name}.html'
    req = requests.get(url, 'html.parser')

    with open('../pages/' + name + '.html', 'w') as f:
        f.write(req.text)
        f.close()