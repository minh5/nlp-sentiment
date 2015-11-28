from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#user credentials to access Twitter API
access_token = "42072314-ayuHnTMP0KOfftqtQ7D6zlqOObW4XLkNUX1ABftsQ"
access_token_secret = "Dqb36M5SjvpkK1UyvAnnTu2XxdMCr9IVMe17EV9ds5EVS"
consumer_key = "9idw1dVNudHIyBoxlETdJLt99"
consumer_secret = "142xtkSXla8Y7uKAid9N2Rt6h8RPUEuy2bd7u2fIFQLzz0zBfJ"


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
    stream.filter(track=['trump', 'donald', 'donald trump'])
