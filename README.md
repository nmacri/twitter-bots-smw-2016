Let's Build a Twitter Bot Together!
=========

Slides, examples and code for "build-a-bot workshop" at Social Media Week NYC 2016.

http://socialmediaweek.org/newyork/events/twitter-bots/

## Getting Started

### Tutorial Notebooks
1. [Setting Up a Twitter Bot in 5 Easy Steps](http://nbviewer.jupyter.org/github/nmacri/twitter-bots-smw-2016/blob/master/notebooks/1%20-%20Setting%20Up%20a%20Twitter%20Bot%20in%205%20Easy%20Steps.ipynb)
 1. [Get you project directory organized](http://nbviewer.jupyter.org/github/nmacri/twitter-bots-smw-2016/blob/master/notebooks/1%20-%20Setting%20Up%20a%20Twitter%20Bot%20in%205%20Easy%20Steps.ipynb#1.-First-things-first,-let's-get-our-project-directory-organized)
 2. [Register a Twitter app](http://nbviewer.jupyter.org/github/nmacri/twitter-bots-smw-2016/blob/master/notebooks/1%20-%20Setting%20Up%20a%20Twitter%20Bot%20in%205%20Easy%20Steps.ipynb#2.-Good,-that-went-smoothly,-now-let's-go-deal-with-twitter)
 3. [Create a Twitter account](https://twitter.com/signup)
 4. [OAuth secret handshake](http://nbviewer.jupyter.org/github/nmacri/twitter-bots-smw-2016/blob/master/notebooks/1%20-%20Setting%20Up%20a%20Twitter%20Bot%20in%205%20Easy%20Steps.ipynb#4.-Final-OAuth-step:-Secret-handshake!)
 5. [Store your secrets somewhere safe](http://nbviewer.jupyter.org/github/nmacri/twitter-bots-smw-2016/blob/master/notebooks/1%20-%20Setting%20Up%20a%20Twitter%20Bot%20in%205%20Easy%20Steps.ipynb#5.-Store-your-secrets-somewhere-safe)
2. What's a Twitter bot anyway?: An MVP Twitter bot that anyone can use
3. What should your bot say?: Markov is just fancy name for autocomplete
4. Kanye autocompletes your social strategy: A simple rules-based markov bot for Socal Media Week.

### Using this Repo to build your own bot

1. `git clone https://github.com/nmacri/twitter-bots-smw-2016.git` 
    - **:confused: "huh, git what?"** --- don't sweat it, you can [download as a zip file](https://github.com/nmacri/twitter-bots-smw-2016/archive/master.zip) instead.
2. cd to your project folder.  in my case it's `cd ~/twitter-bots-smw-2016`
3. If you haven't already, install [virtualenv](https://virtualenv.readthedocs.org/en/latest/installation.html) so you can run this in a clean python environment.
    - **:confused: "err, python's not really my thing?"** ---- it's cool.  There's a javascript example [here](https://github.com/nmacri/twitter-bots-smw-2016/tree/master/examples) but it's kind of janky.  
    - Here are a few things that are way more awesome and useful:
        - [Libraries that support the Twitter API](https://dev.twitter.com/overview/api/twitter-libraries)
        - [RiTa: A toolkit for computational literature](https://rednoise.org/rita/) implemented in Java and Javascript with integrations for Processing, Android, Note, P5.js, Broswerify, Bower, etc.
4. Create an isolated virtual environment for this project to run in: `virtualenv venv`.
5. Activate your virtualenv using `source venv/bin/activate`
6. Once you've activated your virtualenv, you'll need to install some dependencies: `pip install -r requirements.txt`
7. Start by working through the jupyter notebooks in '/notebooks': `cd notebooks && jupyter notebook` (or if you prefer you can [view them online](http://nbviewer.jupyter.org/github/nmacri/twitter-bots-smw-2016/tree/master/notebooks/))

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

- [x] production account
- [x] staging account
- [x] 3-4 test interlocutors

### Testing Plans
- [ ] A fake dataset for testing schedule-driven tweets

### Notebooks
- [x] Setting Up a Twitter Bot in 5 Easy Steps
- [ ] What's a Twitter bot Anyway?: An MVP Twitter bot that anyone can use
- [ ] What should your bot say?: Markov is just fancy name for autocomplete
- [ ] Kanye autocompletes your social strategy: A simple rules-based markov bot for Socal Media Week.


