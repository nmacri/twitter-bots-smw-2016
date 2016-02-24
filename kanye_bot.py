from bot import TwitterBot, MarkovBabbler, TwitterListener
import json
import random

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
    return [smw_program_babbler]#,
            #smw_all_tweets_babbler,
            #smw_recent_tweets_babbler]

def generate_text(seed_generator, in_reply_to=None):
    try:
        if in_reply_to:
            seed = MarkovBabbler(in_reply_to.text).generate_seed()
        else: 
            seed = seed_generator.generate_seed()
        tweet_text = kanye_babbler.generate(seed=seed)
        return tweet_text
    except:
        return generate_text(seed_generator, in_reply_to=in_reply_to)

if __name__ == '__main__':
    # instantiate the bot
    kanye = TwitterBot('test2')
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

    # reply to topical tweets
    try:
        query = """
        (#smwnyc OR "social media" OR "twitter bots" OR "automation" OR #SMWbots OR #SMWbots OR bot OR bots)
        """
        topical_tweets = kanye._api_client.GetSearch(query)
        for tweet in topical_tweets:
            if not kanye.has_replied(tweet):
                text = generate_text(None, in_reply_to=tweet)
                kanye.tweet(text, in_reply_to=tweet)
    except Exception, e:
        print str(e)
        pass

    seed_generator = random.choice(seed_generators)
    text = generate_text(seed_generator)
    kanye.tweet(text)

