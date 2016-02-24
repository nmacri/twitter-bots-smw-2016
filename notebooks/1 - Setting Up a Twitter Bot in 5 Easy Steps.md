
Setting Up a Twitter Bot in 5 Easy Steps
====

1. Get our project directory organized
2. Make a Twitter app
3. Make a Twitter account
4. OAuth secret handshake
5. Store our secrets somewhere safe

### 1. First things first, let's get our project directory organized

if you're running this locally check out [README.md](https://github.com/nmacri/twitter-bots-smw-2016/blob/master/README.md) otherwise skip to the next section...


```python
# cd into your project directory in my case this is, but yours may be different
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

### 2. Good, that went smoothly, now let's go deal with twitter


To run our bot we'll need to use a protocol called [OAuth](https://www.wikiwand.com/en/OAuth) which sounds a little bit daunting, but really it's just a kind of secret handshake that we agree on with twitter so they know that we're cool.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Oauth_logo.svg/239px-Oauth_logo.svg.png) ![](https://49.media.tumblr.com/tumblr_mbbl0uMR8t1ri61zco1_500.gif)

First thing you'll need to do is make an "app".  It's pretty straightforward process that you can go through here https://apps.twitter.com/.  

This is what my settings looked like:

![](http://cl.ly/2o3J0R103s2N/Image%202016-02-20%20at%208.35.10%20PM.png)

In the end you'll get two tokens (`YOUR_APP_KEY` and `YOUR_APP_SECRET`) that you should store somewhere safe.  I'm storing mine in a file called `secrets.json` there is an example (`secrets_example.json`) in the project root directory that you can use as a template.  It looks like this:


```python
f = open('secrets_example.json','rb')
print "".join(f.readlines())
f.close()
```

### 3. Make your Bot's Account!

[Twitter's onboarding process](https://twitter.com/signup) isn't really optimized for the bot use-case, but once you get to the welcome screen you'll be logged in and ready for the next step (iow, you can keep the "all the stuff you love" to yourself).

<br>
<br>
<div class="container" style="width: 80%;">
 <div class="theme-table-image col-sm-5">
   <img src="http://cl.ly/2l2t380q393G/Image%202016-02-20%20at%209.06.21%20PM.png">
 </div>
 <div class="col-sm-2">
 </div>
 <div class="theme-table-image col-sm-5">
   <img src="http://cl.ly/050O2M362Q1B/Image%202016-02-20%20at%209.07.35%20PM.png">
 </div>
</div>




### 4. Final OAuth step: Secret handshake!

Load in your fresh new file of secrets (`secrets.json`)


```python
f = open('secrets.json','rb')
secrets = json.load(f)
f.close()
```

Use a library that knows how to implement OAuth1 (trust me, it's not fun to figure out by scratch).  I'm using [rauth](https://rauth.readthedocs.org/en/latest/) but there are [tons more](https://dev.twitter.com/oauth/overview/single-user) out there.


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

The cells above will open a permissions dialog for you in a new tab:

![](http://cl.ly/2I2L2m1L2e1K/Image%202016-02-20%20at%209.29.46%20PM.png)

**If you're cool w/ it, authorize your app** against your bot user you will then be redirected to the callback url you specified when you set up your app. I get redirected to something that looks like this

`http://127.0.0.1:9999/?oauth_token=JvutuAAAAAAAkfBmbVABUwFD6pI&oauth_verifier=pPktmz2xoFtjysR4DHSlFKcdahuUG`

**It will like an error, but it's not!**,  all you need to do is parse out two parameters from the url they bounce you back to: the `oauth_token` and the `oauth_verifier`.  

Only one more step to go. You are so brave! 


```python
# Once you go through the flow and land on an error page http://127.0.0.1:9999 something
# enter your token and verifier below like so.  The 
# The example below (which won't work until you update the parameters) is from the following url: 
# http://127.0.0.1:9999/?oauth_token=JvutuAAAAAAAkfBmbVABUwFD6pI&oauth_verifier=pPktmz2xoFtjysR4DHSlFKcdahuUGciE

oauth_token='JvutuAAAAAAAkfBmbVABUwFD6pI'
oauth_verifier='pPktmz2xoFtjysR4DHSlFKcdahuUGciE'

session = tw_oauth_service.get_auth_session(request_token,
                                   request_token_secret,
                                   method='POST',
                                   data={'oauth_verifier': oauth_verifier})
```

### 5. Store your secrets somewhere safe


```python
# Copy this guy into your secrets file 

#           {
#            "user_id": "701177805317472256",
#            "screen_name": "SmwKanye",
# HERE ----> "token_key": "YOUR_TOKEN_KEY",
#            "token_secret": "YOUR_TOKEN_SECRET"
#           },
session.access_token
```


```python
# Copy this guy into your secrets file 

#           {
#            "user_id": "701177805317472256",
#            "screen_name": "SmwKanye",
#            "token_key": "YOUR_TOKEN_KEY",
# HERE ----> "token_secret": "YOUR_TOKEN_SECRET"
#           },
session.access_token_secret
```

Awesome, now we have our user access tokens and secret.  Store them in `secrets.json` and test below to see if they work.  You don't really need 3 test accounts, so if you don't want to repeat the process just keep "production".

Finally, test to see that your secrets are good...


```python
f = open('secrets.json','rb')
secrets = json.load(f)
f.close()

tw_api_client = twitter.Api(consumer_key = secrets['twitter']['app']['consumer_key'],
            consumer_secret = secrets['twitter']['app']['consumer_secret'],
            access_token_key = secrets['twitter']['accounts']['production']['token_key'],
            access_token_secret = secrets['twitter']['accounts']['production']['token_secret'],
           )
```


```python
tw_api_client.GetUser(screen_name='SmwKanye').AsDict()
```


```python
tw_api_client.
```

![High Five](http://media3.giphy.com/media/IxJMT1ugyBMdy/giphy.gif)
