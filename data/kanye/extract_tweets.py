## %cd ~/twitter-bots-smw-2016/

import re
from bot import TwitterBot
bot1 = TwitterBot('test1')

def strip_links(text):
    text = re.sub(r"http\S+", "", text, flags=re.MULTILINE)
    return text.encode('ascii','ignore').lower().strip()

tl = tw.GetUserTimeline(screen_name='KanyeWest', count = 200)
f = open('data/kanye/tweets.txt','ab')

while len(tl) > 1:
    for t in tl:
        max_id = t.id
        print max_id
        f.write(strip_links(t.text))
        f.write('\n')
    tl = tw.GetUserTimeline(screen_name='KanyeWest', count = 200, max_id=max_id)
