from bot import TwitterBot, MarkovBabbler, TwitterListener
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

    # reply to outstanding mentions
    mentions_not_replied_to = kanye.get_mentions_not_replied_to()
    print mentions_not_replied_to
    for mention in mentions_not_replied_to:
        text = generate_text(None, in_reply_to=mention)
        kanye.tweet(text, in_reply_to=mention)

    should_i_tweet_now = {0: 0.083333333333333343,
                          1: 0.083333333333333343,
                          2: 0.066666666666666666,
                          3: 0.016666666666666666,
                          4: 0.016666666666666666,
                          12: 0.10000000000000001,
                          13: 0.083333333333333343,
                          14: 0.20000000000000001,
                          15: 0.23333333333333336,
                          16: 0.31666666666666665,
                          17: 0.38333333333333336,
                          18: 0.45000000000000007,
                          19: 0.36666666666666664,
                          20: 0.46666666666666673,
                          21: 0.18333333333333332,
                          22: 0.16666666666666669,
                          23: 0.11666666666666668}

    if random.random() < should_i_tweet_now[datetime.now().hour]:

        seed_generator = random.choice(seed_generators)


        # reply to topical tweets
        try:
            query = """
            (#smwnyc OR "social bots" OR "social media week" OR "twitter bots" OR "twitter bot" OR "social bot" OR #SMWbots OR #SMWbot)
            """
            topical_tweets = kanye._api_client.GetSearch(query)
            for tweet in topical_tweets:
                if not kanye.should_reply(tweet):
                    text = generate_text(seed_generator, in_reply_to=tweet)
                    kanye.tweet(text, in_reply_to=tweet)

        except Exception, e:
            print str(e)
            pass
        
        text = generate_text(seed_generator)
        # kanye.tweet(text)
    else:
        print "not going to tweet now"

