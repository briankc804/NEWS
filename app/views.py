from flask import render_template
from app import app
from .request import get_news,get_sources


# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    #Getting business news
    source = get_sources()
    business_news =get_news('business')
    entertainment_news=get_news('entertainment')
    technology_news=get_news('technology')
    title = 'Home-Welcome to the ultimate news review site'
    
    return render_template('index.html', source = source,title = title,business = business_news,entertainment =entertainment_news,technology =technology_news)

@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
   
    return render_template('news.html',id=news_id)    