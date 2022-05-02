import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News(1234,'wired','How Elon Musk Won Twitter','His weeks-long pursuit of the company has resulted in a $44 billion deal. But how did it happen, and what the hell comes next?','https://www.wired.com/story/elon-musk-buys-twitter-deal/','https://media.wired.com/photos/6266f8d9f2e5a2b3f2ddf24f/191:100/w_1280,c_limit/Elon_twitter_musk_GettyImages-1233956115.jpg','2022-04-25T19:41:32Z','Such social media battles may be unusual when considering a takeover of a massive business, but Musk is himself unusual, says Cary Cooper, a business professor at Manchester Business School. Hes not … [+4004 chars]')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()