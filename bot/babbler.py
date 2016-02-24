from pymarkovchain import MarkovChain
import hashlib
import random
import string, re

class MarkovBabbler(object):
    """docstring for MarkovBabbler"""
    def __init__(self, training_text):
        super(MarkovBabbler, self).__init__()
        ascii_safe_text = ''.join([i if ord(i) < 128 else ' ' for i in training_text])
        self.training_text = ascii_safe_text
        self.train(training_text)

        f = open('data/badwords/full-list-of-bad-words-banned-by-google.txt','rb')
        self.bad_words = [w.replace("\r\n","") for w in f.readlines()]
        f.close()


    def generate_candidate(self, seed=None):
        if seed:
            return self.mc.generateStringWithSeed(seed)
        else:
            return self.mc.generateString()

    def is_valid(self, text_candidate):
        try:
            for bad_word in self.bad_words:
                if bad_word in set([w.lower() for w in text_candidate.split(' ')]):
                    print "Text Candidate rejected for dirty words: %s" % text_candidate
                    return False

            if len(text_candidate) > 140:
                print "Text Candidate rejected for length > 140: %s" % text_candidate
                return False

            if len(text_candidate) < 15:
                print "Text Candidate rejected for length <15"
                return False
        except Exception, e:
            print str(e)
            return False
        
        return True

    def generate(self, seed=None):
        valid = False
        tries = 0
        while not valid and tries < 100:
            try:
                text_candidate = self.generate_candidate(seed=seed)
                valid = self.is_valid(text_candidate)
                tries += 1
            except Exception, e:
                tries += 1
                continue

        if tries < 100:
            return text_candidate
        else:
            raise Exception("can not generate text efficiently too many tries")

    def generate_seed(self):
        seed = " ".join(self.generate().strip().split(" ")[0:random.randint(2,6)])
        regex = re.compile('[%s]' % re.escape('!"$%&\'()*+,-./:;<=>?[\\]^`{|}~'))
        return regex.sub('', seed).capitalize()

    def train(self, training_text):
        m = hashlib.md5(self.training_text)
        self.name = m.hexdigest()
        self.database_filepath = 'data/markov/%s' % self.name

        self.mc = MarkovChain(dbFilePath=self.database_filepath)
        self.mc.generateDatabase(training_text, n=2)
        

