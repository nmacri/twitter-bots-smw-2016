import sqlite3
import twitter

class TweetDatastore(object):
    """docstring for DataStore"""
    def __init__(self, name):
        super(TweetDatastore, self).__init__()
        self.__name = name
        self.__sqlite_db_filename = 'data/tweets/%s.db' % self.__name
        self.__conn = sqlite3.connect(self.__sqlite_db_filename)
        self.__validate_schema()

    def __validate_schema(self):
        sql = """
        CREATE TABLE IF NOT EXISTS `tweets` (
            `status_id` bigint(36) PRIMARY KEY NOT NULL,
            `text` varchar(145) NOT NULL DEFAULT '',
            `created_at` datetime NOT NULL,
            `screen_name` varchar(45) DEFAULT NULL,
            `user_id` bigint(18) NOT NULL,
            `in_reply_to_status_id` bigint(36) NULL,
            `in_reply_to_user_id` bigint(18) NULL,
            `retweeted_status_id` bigint(36) DEFAULT NULL);
        """
        curs = self.__conn.cursor()
        curs.execute(sql)
        self.__conn.commit()

        sql = "CREATE INDEX IF NOT EXISTS in_reply_to_status_id ON tweets (in_reply_to_status_id);"
        curs = self.__conn.cursor()
        curs.execute(sql)
        self.__conn.commit()

        sql = "CREATE INDEX IF NOT EXISTS in_reply_to_user_id ON tweets (in_reply_to_user_id);"
        curs = self.__conn.cursor()
        curs.execute(sql)
        self.__conn.commit()

        sql = "CREATE INDEX IF NOT EXISTS created_at ON tweets (created_at);"
        curs = self.__conn.cursor()
        curs.execute(sql)
        self.__conn.commit()

        sql = """
        CREATE TABLE IF NOT EXISTS `annotations` (
            `status_id` bigint(36) PRIMARY KEY NOT NULL,
            `annotation` varchar(145) NOT NULL DEFAULT '');
        """
        curs = self.__conn.cursor()
        curs.execute(sql)
        self.__conn.commit()

    def __flatten_tweet(self, tweet):
        return {"status_id": str(tweet.id),
                "text": tweet.text,
                "created_at": tweet.created_at,
                "in_reply_to_status_id": str(tweet.in_reply_to_status_id),
                "in_reply_to_user_id": str(tweet.in_reply_to_user_id),
                "retweeted_status_id": str(tweet.retweeted_status.id) if tweet.retweeted_status else None,
                "screen_name": tweet.user.screen_name,
                "user_id": tweet.user.id}

    def store(self, tweets):
        """
        stores tweets

        Params:
        tweets - twitter.Status object or iterable of twitter.Status objects
        """
        try:
            flat_tweets = [self.__flatten_tweet(t) for t in tweets]
        except Exception, e:
            if type(tweets) == twitter.status.Status:
                flat_tweets = [self.__flatten_tweet(tweets)]
            else:
                raise e

        sql = """
        INSERT OR IGNORE INTO tweets (user_id,screen_name,retweeted_status_id,
            status_id,text,created_at,
            in_reply_to_status_id,in_reply_to_user_id)
        VALUES (:user_id,:screen_name,:retweeted_status_id,:status_id,:text,
            :created_at,:in_reply_to_status_id,:in_reply_to_user_id)
        """

        curs = self.__conn.cursor()
        curs.executemany(sql,flat_tweets)
        curs.close()
        self.__conn.commit()

    def annotate(self, tweet, annotation):
        sql = """
        INSERT OR IGNORE INTO annotations (status_id,annotation)
        VALUES (?,?)
        """
        curs = self.__conn.cursor()
        curs.execute(sql,(tweet.id, annotation))
        curs.close()
        self.__conn.commit()
        
