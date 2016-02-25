
## bots should be able to listen

```python
from library import TwitterListener
```
```python
listener = TwitterListener('smw_listener', 
                query="#SMWNYC OR #SMWbot OR to:SmwKanye -:(")
listener.backfill()
```
```python
tweet_text = listener.get_recent_text(40)
print tweet_text[0:288]
```
    @dctweetbounce super excited for @adaptly's #smwnyc panel tomorrow 
    1pm w @ruthyarbs @krisrolla @jessicasherrets & fav @machiz :)htt
    @beaksandgeeks listen to @figbarton, author of the widow  #smwnyc 
    @henrikaufman #smwnyc vous connaissez la vi-are ? virtualit reality ou ralit augmente 

---

## generating text

```python
from library import MarkovBabbler

babbler1 = MarkovBabbler(tweet_text)
babbler2 = MarkovBabbler(yeezy_text)
```
```python
seed = babbler1.generate_seed()
seed
```

    '@its_alicia hire creative weirdos let'

```python
text = babbler1.generate(seed=seed)
text
```

    '@its_alicia hire creative weirdos let them experiment, then let data make them better'

```python
text = babbler2.generate(seed=seed)
text
```

    '@its_alicia hire creative weirdos let them play with the best rapper of all tiiiiiiiiiiiiiiiiiime'

---

@SmwKanye Components

- Four <span style="color:#D75F45">Markov Babblers</span>, trained on different text data sets
  - <small>Recent SMW Tweets</small>
  - <small>All SMW Tweets</small>
  - <small>The SMW Theme Manifesto + Event Titles & Descriptions</small>
  - <small>A lot of Kanye text (tweets, interviews, lyrics, etc.)</small>
- Two <span style="color:#D75F45">Twitter Listeners</span> subscribed to the following queries
  - <small>'#SMWNYC OR "social media week" OR @SMWNYC OR #SMWbot OR @SmwKanye'</small>
  - <small>(#smwnyc OR "social bots" OR "social media week" OR "twitter bots" OR "twitter bot" OR "social bot" OR #SMWbots OR #SMWbot)</small>
- One production <span style="color:#D75F45">Twitter Bot</span> and three test bots

---

# THANK YOU!

![](http://cl.ly/3I111v3J3D3I/Image%202016-02-25%20at%2012.14.50%20AM.png)


