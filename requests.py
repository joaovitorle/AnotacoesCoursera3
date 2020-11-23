#1
import requests

page = requests.get("https://api.datamuse.com/words?rel_rhy=funny") 
print(type(page))
print(page.text[:150]) #print the first 150 characters
print(page.url)

#2

d = {'q': 'violins and guitars', 'tbm': 'isch'}
results = requests.get("https://google.com/search", params = d)
print(results.url)
print(results.text)

#3
import json
import requests
def get_rhymes(words):
    baseurl = "http://api.datamuse.com/words"
    params_diction= {} #Set up an empty dictionary for query parameters
    params_diction["rel_rhy"] = word 
    params_diction["max"] = "3" #get at most 3 results
    resp = requests.get(baseurl, params = params_diction)
    #return the top three words
    word_ds = resp.json()
    return [d['word']] for d in word_ds]
    return resp.json() #return a python object 

print(get_rhymes("funny"))
print(get_rhymes("dash"))

#4
import requests
r = requests.get("http://api.datamuse.com/words", ["rel_rhy","funny"])
print(r.text)
print(r.url)
