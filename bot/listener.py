class TwitterListener(object):
    """docstring for TwitterListener"""
    def __init__(self, arg):
        super(TwitterListener, self).__init__()
        self.arg = arg

    def get_recent_tweets(self):
        """
        hits search api to collect recent relevant tweets
        """
        pass

    def listen(self):
        """
        Subscribes to a twitter stream and stores the result
        """
        pass

    def backfill(self, number_of_tweets):
        """
        hits search api to collect recent relevant tweets and stores the result
        """
        pass
        
