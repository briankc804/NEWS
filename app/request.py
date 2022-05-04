from app import app
import urllib.request,json
from .models import news

News = news.News
Sources =news.Sources

# Getting api key
api_key = app.config['NEWS_API_KEY']


# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]
source_url =app.config["SOURCES_API_BASE_URL"]

def get_news(category): 
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        news_articles = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_articles = process_articles(news_results_list)


    return news_articles

def process_articles(articles_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        articles_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in articles_list:
        id = news_item.get('source')
        title = news_item.get('title')
        description = news_item.get('description')
        url =news_item.get('url')
        urlToImage = news_item.get('urlToImage')
        publishedAt = news_item.get('publishedAt')
        content = news_item.get('content')

        news_object = News(id['id'],title,description,url,urlToImage,publishedAt,content)
        news_results.append(news_object)

    return news_results

def get_sources():

    get_sources_url = source_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        news_updates = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            news_updates = process_sources(sources_results_list)


    return news_updates

def process_sources(sources_list): 

    sources_results = []
    for sources_item in sources_list:
       
        name = sources_item.get('name')
        description = sources_item.get('description')
        url =sources_item.get('url')

        if id:
            sources_object = Sources(name,description,url)   
            sources_results.append(sources_object)
    
   
    return sources_results
   
