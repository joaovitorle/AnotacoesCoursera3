#1
import requests_with_caching
import json

def get_movies_from_tastedive(title):
    url = 'https://tastedive.com/api/similar'
    param = {}
    param['q']= title
    param['type']= 'movies'
    param['limit']= 5
    
    this_page_cache = requests_with_caching.get(url, params=param)
    return json.loads(this_page_cache.text)

get_movies_from_tastedive('Captain Marvel')
get_movies_from_tastedive('Sherlock Holmes')
    

#2

import requests_with_caching
import json


def get_movies_from_tastedive(title):
    endpoint = 'https://tastedive.com/api/similar'
    param = {}
    param['q'] = title
    param['limit'] = 5
    param['type'] = 'movies'

    this_page_cache = requests_with_caching.get(endpoint, params=param)
    return json.loads(this_page_cache.text)


def extract_movie_titles(dic):
    return ([i['Name'] for i in dic['Similar']['Results']])


#3
import requests_with_caching
import json


def get_movies_from_tastedive(title):
    endpoint = 'https://tastedive.com/api/similar'
    param = {}
    param['q'] = title
    param['limit'] = 5
    param['type'] = 'movies'

    this_page_cache = requests_with_caching.get(endpoint, params=param)
    return json.loads(this_page_cache.text)


def extract_movie_titles(dic):
    return ([i['Name'] for i in dic['Similar']['Results']])


def get_related_titles(movie_list):
    li = []
    for movie in movie_list:
        li.extend(extract_movie_titles(get_movies_from_tastedive(movie)))
    return list(set(li))


get_related_titles(["Black Panther", "Captain Marvel"])

#4

import requests_with_caching
import json


def get_movie_data(title):
    endpoint = 'http://www.omdbapi.com/'
    param = {}
    param['t'] = title
    param['r'] = 'json'
    this_page_cache = requests_with_caching.get(endpoint, params=param)

    return json.loads(this_page_cache.text)


get_movie_data("Venom")
get_movie_data("Baby Mama")

#5
import requests_with_caching
import json


def get_movie_data(title):
    endpoint = 'http://www.omdbapi.com/'
    param = {}
    param['t'] = title
    param['r'] = 'json'
    this_page_cache = requests_with_caching.get(endpoint, params=param)
    return json.loads(this_page_cache.text)
print(get_movie_data("Black Panther")['Ratings'][1])
def get_movie_rating(dic):
    ranking = dic['Ratings']
    for dic_item in ranking:
        if dic_item['Source'] == 'Rotten Tomatoes':
            return int(dic_item['Value'][:-1])
    return 0


get_movie_rating(get_movie_data("Deadpool 2"))

#6

import requests_with_caching
import json

def get_movies_from_tastedive(title):
    endpoint = 'https://tastedive.com/api/similar'
    param = {}
    param['q'] = title
    param['limit'] = 5
    param['type'] = 'movies'
    this_page_cache = requests_with_caching.get(endpoint, params=param)
    return json.loads(this_page_cache.text)

def extract_movie_titles(dic):
    list = []
    for i in dic['Similar']['Results']:
        list.append(i['Name'])
    return(list)

def get_related_titles(titles_list):
    list = []
    for i in titles_list:
        new_list = extract_movie_titles(get_movies_from_tastedive(i))
        for i in new_list:
            if i not in list:
                list.append(i)
    print(list)
    return list

def get_movie_data(title):
    endpoint = 'http://www.omdbapi.com/'
    param = {}
    param['t'] = title
    param['r'] = 'json'
    this_page_cache = requests_with_caching.get(endpoint, params=param)
    return json.loads(this_page_cache.text)

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movie_rating(get_movie_data("Deadpool 2"))

def get_movie_rating(data):
    rating = 0
    for i in data['Ratings']:
        if i['Source'] == 'Rotten Tomatoes':
            rating = int(i['Value'][:-1])
            #print(rating)
    return rating 

def get_sorted_recommendations(list):
    new_list = get_related_titles(list)
    new_dict = {}
    for i in new_list:
        rating = get_movie_rating(get_movie_data(i))
        new_dict[i] = rating
    print(new_dict)
    #print(sorted(new_dict, reverse=True))
    return [i[0] for i in sorted(new_dict.items(), key=lambda item: (item[1], item[0]), reverse=True)]

    