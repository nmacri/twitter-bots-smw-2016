

# An MVP Twitter bot that anyone can use

---

<p> Let's <span style="color:#D75F45">simplify</span> and be <span style="color:#D75F45">systematic</span> about the set of <span style="color:#D75F45">interactions</span> we are working with...

Note: Abstraction is a powerful thing it helps us develop more complex, flexible structurs

---

```python
from library import TwitterBot
```
```python
bot1 = TwitterBot('test1')
bot2 = TwitterBot('test2')
bot3 = TwitterBot('test3')

kanye = TwitterBot('production')
```

```python
kanye.tweet('Attendees will learn to like small dogs and cigarettes')
```

<img src="http://cl.ly/131j2J2E281E/Image%202016-02-25%20at%2012.18.43%20AM.png" height=200>

---


```python
# they can talk between the two of them
tweet = bot3.tweet("Testing 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11...")
reply_tweet = bot1.tweet("I can hear you!", in_reply_to=tweet)
```

<img src="http://cl.ly/0o3G433V2402/Image%202016-02-24%20at%2011.29.30%20PM.png" height=200>

```python
# they remember their conversations
bot1.has_replied(tweet)
```
    True

```python
bot3.has_replied(reply_tweet)
```
    False


---

```python
# or they can have a conversation 
tweet = bot1.tweet("Is there anybody out there?")
reply_tweet1 = bot2.tweet("Mr. Watson--come here--I want to see you.", 
                          in_reply_to=tweet)
reply_tweet2 = bot3.tweet("""wait, I thought I was your one and only. 
                          who is @%s?""" % bot1.user.screen_name, 
                          in_reply_to=reply_tweet1)
```

<img src="http://cl.ly/04000W0q0K3h/Image%202016-02-24%20at%2011.33.10%20PM.png" height=300>

---

```python
# they should all be friends
bot1._api_client.CreateFriendship(user_id=bot3.user.id)
bot1._api_client.CreateFriendship(user_id=bot2.user.id)
bot2._api_client.CreateFriendship(user_id=bot3.user.id)
bot2._api_client.CreateFriendship(user_id=bot1.user.id)
bot3._api_client.CreateFriendship(user_id=bot2.user.id)
bot3._api_client.CreateFriendship(user_id=bot1.user.id)
```

---

```python
# and they should all like eachother's posts, why not?
bot1._api_client.CreateFavorite(status=reply_tweet1)
bot1._api_client.CreateFavorite(status=reply_tweet2)

bot2._api_client.CreateFavorite(status=tweet)
bot2._api_client.CreateFavorite(status=reply_tweet2)
# except maybe bot 3, he seems a bit wary of bot 1
```

<img src="http://cl.ly/3x3h2S0N1o1B/download/Image%202016-02-24%20at%2011.35.36%20PM.png" height=300>



