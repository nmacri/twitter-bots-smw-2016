import twitter
import json

f = open('secrets.json','rb')
secrets = json.load(f)
f.close()

class TwitterBot(object):
    """docstring for TwitterBot"""
    def __init__(self, account_name):
        super(TwitterBot, self).__init__()
        self.__app = secrets['twitter']['app']
        self.__account = secrets['twitter']['accounts'][account_name]
        self._api_client = twitter.Api(consumer_key = self.__app['consumer_key'],
                                       consumer_secret = self.__app['consumer_secret'],
                                       access_token_key = self.__account['token_key'],
                                       access_token_secret = self.__account['token_secret'])
        self.user = self._api_client.GetUser(user_id=self.__account['user_id'])

    def tweet(self, text, in_reply_to=None):
        """
        posts an update as the authenticated user

        Args:
        in_reply_to: a Twitter.Status object
        """

        if in_reply_to == None:
            tweet = self._api_client.PostUpdate(text)
        else:
            assert(type(in_reply_to) == twitter.status.Status)
            reply_text = '@%s %s' % (in_reply_to.user.screen_name, text)
            tweet = self._api_client.PostUpdate(reply_text, in_reply_to_status_id = str(in_reply_to.id))

        return tweet


    def generate_text(self, in_reply_to=None):
        pass
        
    def has_replied(self, tweet):
        pass
