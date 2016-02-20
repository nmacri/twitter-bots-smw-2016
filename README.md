Let's Build a Twitter Bot Together
=========

Slides, Examples and code for "build-a-bot workshop" at Social Media Week NYC 2016

http://socialmediaweek.org/newyork/events/twitter-bots/

## TODOs

###  Text Corpora:
- [x] Social Media Week Talk Descriptions
- [ ] Social Media Week Tweet Archive
- [ ] Kanye West Quotes
- [ ] Kanye West Tweets

### Bot Module

- [ ] Build a basic `TwitterBot` class that can be used like this

```python
bot1 = TwitterBot(**kwds)
bot2 = TwitterBot(**kwds)

text = bot1.generate_text()
reply_text = bot2.generate_text(in_reply_to=text)

tweet = bot1.tweet(text)
reply_tweet = bot2.tweet(reply_text, in_reply_to=tweet)
```

- [ ] Build a bot-specific datastore for tweets that can be used like this

```python
bot2.has_replied(tweet) #True
bot1.has_replied(reply_tweet) #False
```

### Listener Module

- [ ] Build a basic `TwitterListener` class that can be used like this

```python
listener = TwitterListener(**kwds)

listener.subscribe() # Subscribes to a twitter stream
listener.backfill(50) # hits REST apis to collect relevant tweets 

listener.get_recent_tweets(6) #retreives tweets
```

### Datastore Module

- [ ] Build a basic local datastore that can support the storage needs of other classes.  It will need:
 - [ ] A `tweets` table
 - [ ] A `annotations` table consisting of 
    - status_id
    - **annotation

### Create Twitter Accounts

- [ ] production account
- [ ] staging account
- [ ] 3-4 test interlocutors

### Testing Plans
- [ ] A fake dataset for testing schedule-driven tweets
- [ ] 


