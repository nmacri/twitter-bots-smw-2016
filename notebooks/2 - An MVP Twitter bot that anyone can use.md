

```python
%cd ~/twitter-bots-smw-2016/
```

    /Users/nickmacri/twitter-bots-smw-2016



```python
from bot import TwitterBot
```

An MVP Twitter bot that anyone can use
====


```python
bot1 = TwitterBot('test1')
bot2 = TwitterBot('test2')
bot3 = TwitterBot('test3')

kanye = TwitterBot('production')
```


```python
kanye.tweet('Attendees will learn to like small dogs and cigarettes')
```




    <twitter.status.Status at 0x110ade950>




```python
# they can talk between the two of them
tweet = bot3.tweet("Testing 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11...")
reply_tweet = bot1.tweet("I can hear you!", in_reply_to=tweet)
```


```python
# they remember their conversations
bot1.has_replied(tweet)
```




    True




```python
bot3.has_replied(reply_tweet)
```




    False




```python
# or they can have a conversation 
tweet = bot1.tweet("Is there anybody out there?")
reply_tweet1 = bot2.tweet("Mr. Watson--come here--I want to see you.", in_reply_to=tweet)
reply_tweet2 = bot3.tweet("wait, I thought I was your one and only. who is @%s?" % bot1.user.screen_name, 
                          in_reply_to=reply_tweet1)
```


```python
# they should all be friends
bot1._api_client.CreateFriendship(user_id=bot3.user.id)
bot1._api_client.CreateFriendship(user_id=bot2.user.id)
bot2._api_client.CreateFriendship(user_id=bot3.user.id)
bot2._api_client.CreateFriendship(user_id=bot1.user.id)
bot3._api_client.CreateFriendship(user_id=bot2.user.id)
bot3._api_client.CreateFriendship(user_id=bot1.user.id)
```




    <twitter.user.User at 0x10b8a6a50>




```python
# and they should all like eachother's posts, why not?
bot1._api_client.CreateFavorite(status=reply_tweet1)
bot1._api_client.CreateFavorite(status=reply_tweet2)

bot2._api_client.CreateFavorite(status=tweet)
bot2._api_client.CreateFavorite(status=reply_tweet2)
# except maybe bot 3 he seems a bit wary of bot 1
```




    <twitter.status.Status at 0x10b8bd550>


