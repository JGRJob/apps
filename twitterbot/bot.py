import tweepy

consumer_key = ''
consumer_secret = ''

key = ''
secret = ''


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)


def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id


def store_last_seen_id(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return


tweets.api.mentions_timeline()
print(tweets.text[0])

# for tweet in tweets:
#     print(f'{tweet.id} - {tweet.text}')
    
