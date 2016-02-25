Let's Build a Twitter Bot Together!
=========

Slides, examples and code for "build-a-bot workshop" at Social Media Week NYC 2016.

http://socialmediaweek.org/newyork/events/twitter-bots/

### Features
- An extensible python-based framework for standing up simple MVP twitter bots
- [Slides](http://nmacri.github.io/twitter-bots-smw-2016/slides) from Nick's Talk "Twitter Bots and The Automation of Everything" at Social Media Week NYC February 22, 2015
- Tutorial [Jupyter Notebooks](http://nbviewer.jupyter.org/github/nmacri/twitter-bots-smw-2016/tree/master/notebooks/) walking through the process of building a bot
- Production code for [@SmwKanye](http://twitter.com/SmwKanye) A simple rules-based markov twitter bot for Social Media Week NYC 2016.
- [A small web-app](http://nmacri.github.io/twitter-bots-smw-2016/examples/app/) example that lets you remix your own Markov Babblers

## Getting Started

### The Bot

[@SmwKanye](http://twitter.com/SmwKanye) is built from the following compontents, all of which are contained in the `/library` module.  Rules are spaghetti-coded together in `kanye_bot.py` and it runs on a once-a-minute cron job.

- Four `MarkovBabbler`, trained on different text data sets
  - <small>Recent SMW Tweets</small>
  - <small>All SMW Tweets</small>
  - <small>The SMW Theme Manifesto + Event Titles & Descriptions</small>
  - <small>A lot of Kanye text (tweets, interviews, lyrics, etc.)</small>
- Two `TwitterListeners` subscribed to the following queries
  - <small>'#SMWNYC OR "social media week" OR @SMWNYC OR #SMWbot OR @SmwKanye'</small>
  - <small>(#smwnyc OR "social bots" OR "social media week" OR "twitter bots" OR "twitter bot" OR "social bot" OR #SMWbots OR #SMWbot)</small>
- One production `TwitterBot` and three test bots

### Slides

[Slides from Nick's Talk "Twitter Bots and The Automation of Everything" at Social Media Week NYC February 22, 2015](http://nmacri.github.io/twitter-bots-smw-2016/slides)

The default keyboard shortcuts are:

- Up, Down, Left, Right: Navigation
- f: Full-screen
- s: Show slide notes
- o: Toggle overview
- . (Period or b: Turn screen black
- Esc: Escape from full-screen, or toggle overview

### Tutorial Notebooks

1. [Setting Up a Twitter Bot in 5 Easy Steps](http://nbviewer.jupyter.org/github/nmacri/twitter-bots-smw-2016/blob/master/notebooks/1%20-%20Setting%20Up%20a%20Twitter%20Bot%20in%205%20Easy%20Steps.ipynb)
 1. [Get you project directory organized](http://nbviewer.jupyter.org/github/nmacri/twitter-bots-smw-2016/blob/master/notebooks/1%20-%20Setting%20Up%20a%20Twitter%20Bot%20in%205%20Easy%20Steps.ipynb#1.-First-things-first,-let's-get-our-project-directory-organized)
 2. [Register a Twitter app](http://nbviewer.jupyter.org/github/nmacri/twitter-bots-smw-2016/blob/master/notebooks/1%20-%20Setting%20Up%20a%20Twitter%20Bot%20in%205%20Easy%20Steps.ipynb#2.-Good,-that-went-smoothly,-now-let's-go-deal-with-twitter)
 3. [Create a Twitter account](https://twitter.com/signup)
 4. [OAuth secret handshake](http://nbviewer.jupyter.org/github/nmacri/twitter-bots-smw-2016/blob/master/notebooks/1%20-%20Setting%20Up%20a%20Twitter%20Bot%20in%205%20Easy%20Steps.ipynb#4.-Final-OAuth-step:-Secret-handshake!)
 5. [Store your secrets somewhere safe](http://nbviewer.jupyter.org/github/nmacri/twitter-bots-smw-2016/blob/master/notebooks/1%20-%20Setting%20Up%20a%20Twitter%20Bot%20in%205%20Easy%20Steps.ipynb#5.-Store-your-secrets-somewhere-safe)
2. [What's a Twitter bot anyway?: An MVP Twitter bot that anyone can use](http://nbviewer.jupyter.org/github/nmacri/twitter-bots-smw-2016/blob/master/notebooks/2%20-%20An%20MVP%20Twitter%20bot%20that%20anyone%20can%20use.ipynb)
3. [What should your bot say?: Markov is just fancy name for autocomplete](http://nbviewer.jupyter.org/github/nmacri/twitter-bots-smw-2016/blob/master/notebooks/3%20-%20What%20should%20your%20bot%20say%3F.ipynb)

### Using this Repo to build your own bot

1. `git clone https://github.com/nmacri/twitter-bots-smw-2016.git` 
    - **:confused: "huh, git what?"** --- don't sweat it, you can [download as a zip file](https://github.com/nmacri/twitter-bots-smw-2016/archive/master.zip) instead.
2. cd to your project folder.  in my case it's `cd ~/twitter-bots-smw-2016`
3. If you haven't already, install [virtualenv](https://virtualenv.readthedocs.org/en/latest/installation.html) so you can run this in a clean python environment.
    - **:confused: "err, python's not really my thing?"** ---- it's cool.  There's a javascript example [here](http://nmacri.github.io/twitter-bots-smw-2016/examples/app/), but it's kind of janky.  
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
- [x] Social Media Week Tweet Archive
- [x] Kanye West Quotes
- [x] Kanye West Tweets

### Bot Module

- [x] Build a basic `TwitterBot` class that can be used like this

```python
bot1 = TwitterBot(**kwds)
bot2 = TwitterBot(**kwds)

text = bot1.generate_text()
reply_text = bot2.generate_text(in_reply_to=text)

tweet = bot1.tweet(text)
reply_tweet = bot2.tweet(reply_text, in_reply_to=tweet)
```

- [x] Build a bot-specific datastore for tweets that can be used like this

```python
bot2.has_replied(tweet) #True
bot1.has_replied(reply_tweet) #False
```

### Listener Module

- [x] Build a basic `TwitterListener` class that can be used like this

```python
listener = TwitterListener(**kwds)

listener.backfill(50) # hits REST apis to collect relevant tweets 

listener.get_recent_tweets(6) #retreives tweets
```

### Datastore Module

- [x] Build a basic local datastore that can support the storage needs of other classes.  It will need:
 - [x] A `tweets` table


### Create Twitter Accounts

- [x] production account
- [x] staging account
- [x] 3-4 test interlocutors

### Testing Plans
- [x] A fake dataset for testing schedule-driven tweets

### Notebooks
- [x] Setting Up a Twitter Bot in 5 Easy Steps
- [x] What's a Twitter bot anyway?: An MVP Twitter bot that anyone can use
- [x] What should your bot say?: Markov is just fancy name for autocomplete
- [x] Kanye autocompletes your social strategy: A simple rules-based markov bot for Socal Media Week.

### Server
- [x] git deployment on production server

### Slides
- [x] Reaveal templates and build framework

### Examples
- [x] Node app working locally
- [x] Node app working on gh-pages
- [x] Training selectors on web app

### Documentation
- [ ] Docstrings on framework library
- [x] Readme description of framework library


