from bot import TwitterBot, MarkovBabbler, TwitterListener
import json
import random

def get_listener():
    """
    instantate the listener and backfill recent tweets
    """
    smw_listener = TwitterListener('smw', 
                                   query='#SMWNYC OR #SMWbot OR @SmwKanye')
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
    smw_tweet_text_all = smw_listener.get_recent_text(500)
    smw_tweet_text_recent = smw_listener.get_recent_text(20)

    # make some markov babblers
    smw_program_babbler = MarkovBabbler(smw_program_text)
    smw_all_tweets_babbler = MarkovBabbler(smw_tweet_text_all)
    smw_recent_tweets_babbler = MarkovBabbler(smw_tweet_text_recent)
    return [smw_program_babbler,
            smw_all_tweets_babbler]#,
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
    kanye = TwitterBot('test1')
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

    if random.random() < .5:
        seed_generator = seed_generators[0]
    else:
        seed_generator = random.choice(seed_generators)
    text = generate_text(seed_generator)
    kanye.tweet(text)

