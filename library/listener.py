import twitter
import random
import json
import re

from datastore import TweetDatastore

f = open('secrets.json','rb')
secrets = json.load(f)
f.close()

class TwitterListener(object):
    """docstring for TwitterListener"""
    def __init__(self, listener_name, query=None):
        super(TwitterListener, self).__init__()
        self.listener_name = listener_name
        self.query = query
        self.__app = secrets['twitter']['app']
        self.__accounts = secrets['twitter']['accounts']
        self.__set_twitter_api_tokens()
        self.db = TweetDatastore(listener_name)
        self.__set_max_id()

    def __set_twitter_api_tokens(self):
        acct = random.choice(self.__accounts.values())
        self._api_client = twitter.Api(consumer_key = self.__app['consumer_key'],
                                       consumer_secret = self.__app['consumer_secret'],
                                       access_token_key = acct['token_key'],
                                       access_token_secret = acct['token_secret'])

    def __set_max_id(self):
        sql = """
        SELECT max(status_id)
        FROM tweets
        """
        curs = self.db._TweetDatastore__conn.cursor()
        curs.execute(sql)
        max_id = curs.fetchone()[0]
        curs.close()
        self.__max_id = max_id

    def clean_tweet_text(self, text):
        text = re.sub(r"http\S+", "", text, flags=re.MULTILINE)
        text = text.encode('ascii','ignore').lower().strip()
        text = text.replace("&amp;","&")
        text = text.replace("rt ","")
        text = text.replace(": "," ")
        return text


    def get_recent_tweets(self, since_id=None):
        """
        hits search api to and returns a list of recent relevant tweets
        """ 
        tweets = self._api_client.GetSearch(term=self.query, count=100, result_type='recent')
        if since_id:
            try:
                while min([t.id for t in tweets]) > since_id:
                    more_tweets = self._api_client.GetSearch(term=self.query, count=100, result_type='recent', since_id=since_id)
                    tweets.extend(more_tweets)
            except Exception, e:
                pass
        return tweets

    def backfill(self):
        """
        hits search api to collect recent relevant tweets and stores the result
        """
        if self.__max_id:
            tweets = self.get_recent_tweets(since_id=self.__max_id)
        else:
            tweets = self.get_recent_tweets(since_id=self.__max_id)
        self.db.store(tweets)
        self.__set_max_id()

    def get_recent_text(self, number_of_tweets):
        sql = """
        SELECT text
        from tweets
        ORDER BY status_id DESC
        limit ?
        """
        curs = self.db._TweetDatastore__conn.cursor()
        curs.execute(sql,(number_of_tweets,))
        text = "\n".join([t[0] for t in curs.fetchall()])
        curs.close()
        return self.clean_tweet_text(text)

