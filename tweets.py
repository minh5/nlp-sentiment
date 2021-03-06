import os

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#user credentials to access Twitter API
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_SECRET')
consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['marco rubio',"Marco Rubio",
    'donald trump','Donald Trump',
    'ted cruz','Ted Cruz',
    'ben carson','Ben Carson',
    'chris christie','Chris Christie',
    'jeb bush','Jeb Bush',
    'john kasich','John Kasich',
    'rand paul','Rand Paul'
    'gopdebate','GOPDebate',
    ])
