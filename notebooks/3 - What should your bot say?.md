

```python
%cd ~/twitter-bots-smw-2016/
from pymarkovchain import MarkovChain
import json
import random
```

Markov is just fancy name for autocomplete
===


```python
f = open('data/smw/talks.ldjson','rb')
talks = [json.loads(l) for l in f.readlines()]
talk_text = "\n".join([t['name']+" "+t['description'] for t in talks])
f.close()

f = open('data/kanye/quotes.txt','rb')
yeezy_text = "\n".join([l for l in f.readlines()])
f.close()
```


```python
mc1 = MarkovChain(dbFilePath='data/markov')
mc1.generateDatabase(talk_text, n=2)

mc2 = MarkovChain(dbFilePath='data/markov')
mc2.generateDatabase(yeezy_text, n=2)
```


```python
mc2.generateDatabase()
```


```python
mc1.generateString()
```


```python
import nltk

talk_title = mc1.generateString().lower().strip().encode('ascii','ignore')
text = nltk.word_tokenize(talk_title)
nltk.pos_tag(text)
```


```python
def get_talk_title_seed():
    talk_title = mc1.generateString().lower().strip().encode('ascii','ignore')
    rand_int = random.randint(0,len(talk_title.split(' '))-3)
    seed = " ".join(talk_title.split(' ')[rand_int:rand_int+random.randint(3,5)])
    return seed
    
def tweet_like_kayne():
    seed = get_talk_title_seed()
    try:
        candidate = mc2.generateStringWithSeed(seed)
        return candidate
    except Exception, e:
        print str(e)
        return tweet_like_kayne_about_social_media_week_talks()
    
tweet_like_kayne_about_social_media_week_talks()
```


```python

```

## Twitter Listener


```python
%cd ~/twitter-bots-smw-2016/
```


```python
from bot import TwitterListener
```


```python
self = TwitterListener('smw_listener', query="#SMWNYC OR #SMWbot OR to:SmwKanye -:(")
```


```python
self.backfill()
```


```python
recent_tweet_text = self.get_recent_text(40)
mc3 = MarkovChain(dbFilePath='./markov')
mc3.generateDatabase(recent_tweet_text, n=3)
```


```python
def get_recent_tweet_seed():
    text = mc3.generateString()
    rand_int = random.randint(0,len(text.split(' '))-5)
    seed = " ".join(text.split(' ')[rand_int:rand_int+random.randint(3,5)])
    return seed

def tweet_like_kayne():
    seed = get_recent_tweet_seed()
    try:
        candidate = mc2.generateStringWithSeed(seed)
        return candidate
    except Exception, e:
        print str(e)
        return tweet_like_kayne()
    
tweet_like_kayne()
```

## Babbler


```python
%cd ~/twitter-bots-smw-2016/
```

    /Users/nickmacri/twitter-bots-smw-2016



```python
from pymarkovchain import MarkovChain
import json
import random

f = open('data/smw/talks.ldjson','rb')
talks = [json.loads(l) for l in f.readlines()]
talk_text = "\n".join([t['name']+" "+t['description'] for t in talks])
f.close()

f = open('data/kanye/quotes.txt','rb')
yeezy_text = "\n".join([l for l in f.readlines()])
f.close()
```


```python
from bot import MarkovBabbler
```


```python
kanye = MarkovBabbler(yeezy_text)
smw = MarkovBabbler(talk_text)
```

    WARNING:root:Database file corrupt or not found, using empty database
    WARNING:root:Database file corrupt or not found, using empty database



```python
seed = smw.generate_seed()
kanye.generate(seed=seed)
```

    Text Candidate rejected for length > 140: The Revolution Will Be Snapped: How Messaging Apps are Changing Social Change Is Snapchat just the social team, and earn more organizational resources





    u'Youll turn your kin into an enemy'


