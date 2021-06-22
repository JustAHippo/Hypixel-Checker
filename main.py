import requests
from bs4 import BeautifulSoup
URL = 'https://hypixel.net/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='progress')
try:
    final = results.prettify()
    ooh = final.replace('<progress id="progress" max="100" value="', "")
    AAA = ooh.replace('">', "")
    done = AAA.replace(f"</progress>", "")
    bish = done.replace("\n", "") 
    print("Hypixel is " + bish + f"% done!")
except AttributeError:
    print('That\'s strange... Did Hypixel go back up? If not, you might be getting fuckin ratelimited lol.')
