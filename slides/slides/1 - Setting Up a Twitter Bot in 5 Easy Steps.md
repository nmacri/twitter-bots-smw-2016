
![](http://www.explainxkcd.com/wiki/images/b/b2/twitter_bot.png)

---

# Setting Up a Twitter Bot in 5 Easy Steps

1. Get our project directory organized
2. Make a Twitter app
3. Make a Twitter account
4. OAuth secret handshake
5. Store our secrets somewhere safe

---

### Step 1: Get Organized!

https://github.com/nmacri/twitter-bots-smw-2016/

```bash
git clone https://github.com/nmacri/twitter-bots-smw-2016.git
```

```python
# cd into your project directory 
# in my case this is, but yours may be different
%cd ~/twitter-bots-smw-2016/
```

```python
# install dependencies if you haven't already :)
!pip install -r requirements.txt
```

```python
# import your libraries 
import twitter
import json
import webbrowser
from rauth import OAuth1Service
```

Note: Let's get our project directory organized (we're building a robot)

---

https://github.com/nmacri/twitter-bots-smw-2016/

![](http://cl.ly/1x1j1w2Y0j1E/Bitmap.png)

---

### Now let's go deal with twitter...

![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Oauth_logo.svg/239px-Oauth_logo.svg.png) 

![](https://49.media.tumblr.com/tumblr_mbbl0uMR8t1ri61zco1_500.gif)

Note: To run our bot we'll need to use a protocol called [OAuth](https://www.wikiwand.com/en/OAuth) which sounds a little bit daunting, but really it's just a kind of secret handshake that we agree on with twitter so they know that we're cool.

---

### Step 2: Register a Twitter "app"

https://apps.twitter.com/

![](http://cl.ly/2o3J0R103s2N/Image%202016-02-20%20at%208.35.10%20PM.png)

Note: This is what my settings looked like.  **T** In the end you'll get two tokens (`YOUR_APP_KEY` and `YOUR_APP_SECRET`) that you should store somewhere safe.  I'm storing mine in a file called `secrets.json` there is an example (`secrets_example.json`) in the project root directory that you can use as a template. 

---

<section id="majorkey1" data-state="majorkey1"> Major :key:</section>

---

### Step 3: Make your Bot's Account!

<img src="http://cl.ly/2l2t380q393G/Image%202016-02-20%20at%209.06.21%20PM.png" width=400>
<span width=20></span>
<img src="http://cl.ly/050O2M362Q1B/Image%202016-02-20%20at%209.07.35%20PM.png" width=400>

Note: [Twitter's onboarding process](https://twitter.com/signup) isn't really optimized for the bot use-case, but once you get to the welcome screen you'll be logged in and ready for the next step (iow, you can keep the "all the stuff you love" to yourself).

---

### Step 4: Secret handshake! 

<p> <section id="majorkey2" data-state="majorkey2"> :key: -> secrets.json </section> </p>

```python
f = open('secrets.json','rb')
secrets = json.load(f)
f.close()
```

---

Use a library that knows how to implement OAuth1.  I'm using [rauth](https://rauth.readthedocs.org/en/latest/) but there are [tons more](https://dev.twitter.com/oauth/overview/single-user) out there.

```python
tw_oauth_service = OAuth1Service(
    consumer_key=secrets['twitter']['app']['consumer_key'],
    consumer_secret=secrets['twitter']['app']['consumer_secret'],
    name='twitter',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authorize',
    request_token_url='https://api.twitter.com/oauth/request_token',
    base_url='https://api.twitter.com/1.1/')
```

```python
request_token, request_token_secret = tw_oauth_service.get_request_token()
url = tw_oauth_service.get_authorize_url(request_token=request_token)
webbrowser.open_new(url)
```

Note: (trust me, it's not fun to figure out by scratch).  T The cells above will open a permissions dialog for you in a new tab

---

![](http://cl.ly/2I2L2m1L2e1K/Image%202016-02-20%20at%209.29.46%20PM.png)


Note: **If you're cool w/ it, authorize your app** against your bot user you will then be redirected to the callback url you specified when you set up your app. I get redirected to something that looks like this

---

![](http://cl.ly/3R3S3r3a2h0k/Image%202016-02-24%20at%206.23.05%20PM.png)

**It will like an error, but it's not!**

Note: all you need to do is parse out two parameters from the url they bounce you back to: the `oauth_token` and the `oauth_verifier`.  

---

Only one more step to go. You are so brave! 

```python
# copy these from the url
oauth_token='JvutuAAAAAAAkfBmbVABUwFD6pI'
oauth_verifier='pPktmz2xoFtjysR4DHSlFKcdahuUGciE'

session = tw_oauth_service.get_auth_session(request_token,
            request_token_secret,
            method='POST',
            data={'oauth_verifier': oauth_verifier})

# store  session.access_token, and session.access_token_secret somewhere safe
```

---

### Step 5: Store your secrets somewhere safe


<section id="majorkey3" data-state="majorkey3" style="bottom:50px; display: block;"> major :key: -> secrets.json </section>

---

![High Five](http://media3.giphy.com/media/IxJMT1ugyBMdy/giphy.gif)
