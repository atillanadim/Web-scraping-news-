import requests

def News():
  #BBC news api
  #following query parameters are used 
  #source, sortBy and apiKey
  query_params = {
    "source" : "bbc-news", 
    "sortyBy" : "top", 
    "apiKey" : "35a44aa5866548e5bed445da5ec6ac61"
  }
  main_url = "https://newsapi.org/v1/articles"

  #fetching data in json format 
  res = requests.get(main_url, params= query_params)
  open_bbc_page = res.json()

  #GETTING ALL ARTICLES IN A STRING ARTICLE 
  article = open_bbc_page["articles"]

  #empty list wich will
  #contain all trending News
  results = []

  for ar in article:
    results.append(ar["title"])

  for i in range(len(results)):

    #printing all  trending News
    print(i + 1, results[i])

  #to read the news  out loud for us
  from win32com.client import Dispatch
  speak = Dispatch("SAPI.Spvoice")
  speak.Speak(results)

#driver code

if __name__ == '__main__':

  #function call
  News()