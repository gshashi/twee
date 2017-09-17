import twitter
from pprint import pprint
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from pprint import pprint
#for commit

#Variables that contains the user credentials to access Twitter API
access_token = "83331991-fwhLCbRHM4fOBcwGb9BVNV8WmEtKTE9uQpAhyMjz8"
access_token_secret = "uMb5KJkdpmOYvRTIttWxij67FBcZ9wwZ0Fqd6TWcprkId"
consumer_key = "uluRcZNrAfC9RVOCrGWMFyIkV"
consumer_secret = "r9mcByvaeagr0ZJ29cK4OOZcG2feG1SYFBf2V06v0X5ULucWgx"

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        pprint(data)
        return True

    def on_error(self, status):
        pprint(status)

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['Modi', 'Rahul'])