from library import TwitterBot, MarkovBabbler, TwitterListener
import json
import random
from datetime import datetime

def get_listener():
    """
    instantate the listener and backfill recent tweets
    """
    smw_listener = TwitterListener('smw', 
                                   query='#SMWNYC OR "social media week" OR @SMWNYC OR #SMWbot OR @SmwKanye')
    try:
        smw_listener.backfill()
    except:
        pass
    return smw_listener

def get_kanye_babbler():
    f = open('data/kanye/quotes.txt','rb')
    yeezy_text = "\n".join([l for l in f.readlines()])
    f.close()
    return MarkovBabbler(yeezy_text)

def get_smw_seed_generators():
    # load text data sets
    f = open('data/smw/talks.ldjson','rb')
    talks = [json.loads(l) for l in f.readlines()]
    smw_program_text = " ".join([t['name']+" "+t['description'] for t in talks])
    smw_program_text = smw_program_text + "\n".join([l for l in f.readlines()])
    f.close()
    smw_tweet_text_all = smw_listener.get_recent_text(1000)
    smw_tweet_text_recent = smw_listener.get_recent_text(25)

    # make some markov babblers
    smw_program_babbler = MarkovBabbler(smw_program_text)
    smw_all_tweets_babbler = MarkovBabbler(smw_tweet_text_all)
    smw_recent_tweets_babbler = MarkovBabbler(smw_tweet_text_recent)
    return [smw_program_babbler,
            smw_all_tweets_babbler,
            smw_recent_tweets_babbler]

def generate_text(seed_generator, in_reply_to=None):
    try:
        if in_reply_to:
            if random.random() < .5:
                seed = MarkovBabbler(in_reply_to.text).generate_seed()
            else:
                seed = kanye_babbler.generate_seed()
        else: 
            seed = seed_generator.generate_seed()
        tweet_text = kanye_babbler.generate(seed=seed)
        return tweet_text
    except:
        return generate_text(seed_generator, in_reply_to=in_reply_to)

if __name__ == '__main__':
    # instantiate the bot
    kanye = TwitterBot('production')
    kanye.generate_text = generate_text

    smw_listener = get_listener()
    seed_generators = get_smw_seed_generators()

    kanye_babbler = get_kanye_babbler()

    if random.random() < .2:
        # reply to outstanding mentions
        mentions_not_replied_to = kanye.get_mentions_not_replied_to()
        print mentions_not_replied_to
        for mention in mentions_not_replied_to:
            text = generate_text(None, in_reply_to=mention)
            kanye.tweet(text, in_reply_to=mention)

    should_i_tweet_now = {0: 0.072916666666666671,
                         1: 0.072916666666666671,
                         2: 0.058333333333333334,
                         3: 0.014583333333333334,
                         4: 0.014583333333333334,
                         5: 0,
                         6: 0,
                         7: 0,
                         8: 0,
                         9: 0,
                         10: 0,
                         11: 0,
                         12: 0.087500000000000008,
                         13: 0.072916666666666671,
                         14: 0.17500000000000002,
                         15: 0.20416666666666669,
                         16: 0.27708333333333335,
                         17: 0.3354166666666667,
                         18: 0.39375000000000004,
                         19: 0.3208333333333333,
                         20: 0.40833333333333338,
                         21: 0.16041666666666665,
                         22: 0.14583333333333334,
                         23: 0.10208333333333335}

    if random.random() < should_i_tweet_now[datetime.now().hour]:

        seed_generator = random.choice(seed_generators)

        # reply to topical tweets
        try:
            query = """
            (#smwnyc OR "social bots" OR "social media week" OR "twitter bots" OR "twitter bot" OR "social bot" OR #SMWbots OR #SMWbot)
            """
            topical_tweets = kanye._api_client.GetSearch(query)
            for tweet in topical_tweets:
                if random.random() < .05:
                    if not kanye.should_reply(tweet):
                        text = generate_text(seed_generator, in_reply_to=tweet)
                        kanye.tweet(text, in_reply_to=tweet)

        except Exception, e:
            print str(e)
            pass
        
        text = generate_text(seed_generator)
        kanye.tweet(text)
    else:
        print "not going to tweet now"

