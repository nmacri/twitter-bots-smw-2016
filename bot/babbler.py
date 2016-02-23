from pymarkovchain import MarkovChain


f = open('data/smw/talks.ldjson','rb')
talks = [json.loads(l) for l in f.readlines()]
talk_text = "\n".join([t['name']+" "+t['description'] for t in talks])
f.close()

f = open('data/kanye/quotes.txt','rb')
yeezy_text = "\n".join([l for l in f.readlines()])
f.close()

class MarkovBabbler(object):
    """docstring for MarkovBabbler"""
    def __init__(self, training_data):
        super(MarkovBabbler, self).__init__()
        self.arg = arg

    def generate(self, seed=None):
        return "example text"

    def train():
        pass
        
