
Kanye autocompletes your social strategy: A simple rules-based markov bot for Social Media Week.
====


```python
%cd ~/twitter-bots-smw-2016/
```

    /Users/nickmacri/twitter-bots-smw-2016



```python
from library import TwitterBot, MarkovBabbler, TwitterListener
import json
```


```python
# instantiate the bot
kanye = TwitterBot('test1')

# instantate the listener and backfill recent tweets
smw_listener = TwitterListener('smw', 
                               query='#SMWNYC OR #SMWbot OR @SmwKanye')
try:
    smw_listener.backfill()
except:
    pass

# load text data sets
f = open('data/smw/talks.ldjson','rb')
talks = [json.loads(l) for l in f.readlines()]
smw_program_text = " ".join([t['name']+" "+t['description'] for t in talks])
smw_program_text = smw_program_text + "\n".join([l for l in f.readlines()])
f.close()

f = open('data/kanye/quotes.txt','rb')
yeezy_text = "\n".join([l for l in f.readlines()])
f.close()

smw_tweet_text_all = smw_listener.get_recent_text(500)
smw_tweet_text_recent = smw_listener.get_recent_text(20)
```


```python
kanye_babbler = MarkovBabbler(yeezy_text)
smw_program_babbler = MarkovBabbler(smw_program_text)
smw_all_tweets_babbler = MarkovBabbler(smw_tweet_text_all)
smw_recent_tweets_babbler = MarkovBabbler(smw_tweet_text_recent)

seed_generators = [smw_program_babbler,
                   smw_all_tweets_babbler,
                   smw_recent_tweets_babbler]
```

    WARNING:root:Database file corrupt or not found, using empty database
    WARNING:root:Database file corrupt or not found, using empty database
    WARNING:root:Database file corrupt or not found, using empty database
    WARNING:root:Database file corrupt or not found, using empty database



```python
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

generate_text(smw_all_tweets_babbler)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-4-039c82e69eb8> in <module>()
         10         return generate_text(seed_generator, in_reply_to=in_reply_to)
         11 
    ---> 12 generate_text(smw_all_tweets_babbler)
    

    NameError: name 'smw_all_tweets_babbler' is not defined



```python
b = TwitterBot('production')
b.tweet('Data scientists to do award shows for the people')
```




    <twitter.status.Status at 0x1089d0910>




```python
import string
string.punctuation
```




    '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'




```python
def generate_kanye_text(in_reply_to=None):
    if in_reply_to:
        pass
    else:
        seed_text = smwtalkdescription_babbler
        return kanye_babbler.generate()


kanye.generate_text()
```




    'you should overide this method'




```python
query = """
(#smwnyc OR "social media" OR "twitter bots" OR "automation" OR #SMWbots OR #SMWbots OR bot OR bots)
"""
tweets = kanye._api_client.GetSearch(query)
```


```python
[t.text for t in tweets]
```




    [u'Social Media is a Hallucinogenic Drug.',
     u'Social media machine in action!\ncc: @gauravcsawant @abhijitmajumder @AdityaRajKaul https://t.co/z2r8JLtOaF',
     u'Cristiano Ronaldo becomes the first athlete to exceed 200,000,000 social media followers: https://t.co/bRxu8GBUmU https://t.co/F8QBGX0rHU',
     u'@pengo_bot \u3079\u3001\u3079\u3064\u306b\u3042\u3093\u305f\u306e\u305f\u3081\u306b\u624b\u7fbd\u5148\u7372\u3063\u3066\u304d\u305f\u308f\u3051\u3058\u3083\u306a\u3044\u3093\u3060\u304b\u3089\uff01',
     u'RT @Alchemist_DO: https://t.co/S4TEWhYUjt\n\uc640 \uc774\uc5b4\uc9d1\ub2c8\ub2e4.\n-\n"\uc774\uc81c \ubc18\ud56d\uc774 \uc880 \uc0ac\uadf8\ub77c\ub4e4\uc5c8\ub124."\n"\uadf8 \uc0ac\ub78c\uc774 \ub2f9\uc2e0\uc744 \ucc3e\uc544\ub0b4\uba74 \uc8fd\uc77c \uac70\uc608\uc694."\n"\uc0c1\uad00 \uc5c6\uc5b4, \uc774\ubbf8 \ubc84\ub9b0 \ubaa9\uc228."\n\n@vampire_BH_bot https:\u2026',
     u'@pine_ayase_bot \u884c\u3063\u3066\u304d\u307e\u30595\uff0a\xa5',
     u'\u3053\u308c\u306f\u2026',
     u'@JinUzuki_bot \u307e\u3068\u3082\u306b\u6b7b\u306d\u308b\u3068\u601d\u3046\u306a\u3088\u3001\u30a6\u30c5\u30ad!!',
     u'RT @marketersp: 8 Social Media Tips to Increase Customer Loyalty https://t.co/o7w9oMvuel',
     u'@MisonoSenri_bot \u3046\u30fc\u3093\u3068\u3001\u4f55\u304b\u8a00\u3063\u305f\u304b\u306a\uff1f',
     u'@ametan2013_bot \u3084\u3081\u3066\u3055\u3057\u3042\u3052\u308d',
     u'@Liu_Feilong_Bot \u3053\u306e\u30aa\u30ec\u306b\u624b\u306b\u5165\u308c\u3089\u308c\u306a\u3044\u3082\u306e\u306f\u4f55\u3082\u306a\u3044',
     u'\u3044\u3064\u307e\u3067\u98df\u3079\u3066\u3093\u306e\u3063(\u30c6\u30e9\u65e9\u53e3)',
     u'\u3010\u99c5\u7d39\u4ecb\u3011\u65b0\u5e84\u30fb\u30fb\u30fb\u5c71\u5f62\u7dda\u306f\u3053\u3053\u304c\u7d42\u7740&amp;\u8d77\u70b9\u99c5\u3002\u79cb\u7530\u65b9\u9762\u306e\u5965\u7fbd\u672c\u7dda\u306f\u540c\u4e00\u30db\u30fc\u30e0\u3067\u4e57\u308a\u63db\u3048\u3067\u304d\u308b\u3088\uff01\u9014\u4e2d\u3067\u9678\u7fbd\u6771\u7dda\u3068\u4e26\u8d70\u30d0\u30c8\u30eb\u3092\u3057\u3061\u3083\u3046w',
     u'@benymd_bot']




```python
import pandas.io.sql as psql
from dateutil.parser import parse

sql = """
SELECT created_at
from tweets
"""
df = psql.read_sql(sql,smw_listener.db._TweetDatastore__conn)
```


```python
tweets = smw_listener._api_client.GetUserTimeline(screen_name='SMWNYC', count= 200)
```


```python
import pandas as pd
from dateutil.parser import parse
df = pd.DataFrame([t.AsDict() for t in tweets])
```


```python
df['hour'] = df.created_at.apply(lambda t: parse(t).hour)
hour_counts = df.groupby('hour').count().created_at

dict(175 * ((hour_counts.apply(float) / hour_counts.sum()) / 60))
```




    {0: 0.072916666666666671,
     1: 0.072916666666666671,
     2: 0.058333333333333334,
     3: 0.014583333333333334,
     4: 0.014583333333333334,
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




```python
len(smw_listener.get_recent_text(50))
```




    5101




```python
tweet = kanye.tweet('xxlkdxlxxlxxx')
```


```python
kanye.db.annotate(tweet,"do not reply")
```


```python
kanye.should_reply(tweet)
```




    False




```python
kanye._api_client.CreateFavorite(status=)
```
