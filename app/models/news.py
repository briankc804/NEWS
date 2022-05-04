


class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,id,title,description,url,urlToImage,publishedAt,content):
        self.id =id
        self.title = title
        self.description = description
        self.url= url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content

class Sources:

    def __init__(self,id,name,description,url):
        self.id =id
        self.name = name
        self.description = description
        self.url= url
       