from bs4 import BeautifulSoup as BS
import requests as re
Lan_Dict = {  "HINDI" : "hi" , "ENGLISH" : "en" , "MARATHI": "mr"}

class ScrapeIMDBTitle():
  def __init__(self):
    self.base_url = "https://www.imdb.com/search/title/"
    self.headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
  def getScrap(self,lan,geners):
    try:
         lan = Lan_Dict[lan.upper()]
         list_genr = ','.join(genr if isinstance(geners,list) else geners for genr in geners )
         new_url = self.base_url  + f"?title_type=feature&user_rating=7,10&genres={list_genr}&languages={lan}"
         resp = re.get(new_url,headers=self.headers)
         return BS(resp.content,"html5lib")
    except Exception as e:
         print(f"Problem while accessing website {e}")
  def getIMDBTitles(self,lan,geners):
    IMDBId = []
    soup = self.getScrap(lan,geners)
    rows = soup.findAll('a',attrs={'class':'ipc-title-link-wrapper'})
    for row in rows :
      href = row.get('href')
      Id = href.split("/")[2]
      IMDBId.append(Id)
    return IMDBId

