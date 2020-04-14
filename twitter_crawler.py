#!/usr/bin/python

# sudo apt-get install python3-dev libmysqlclient-dev
# pip3 install mysqlclient --user
# pip3 install tweepy --user

import json
import tweepy
import MySQLdb
import urllib.parse
import urllib.request

####input your credentials here
consumer_key        = 'xxx'
consumer_secret     = 'xxx'
access_token        = 'xxx-xxx'
access_token_secret = 'xxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

tweets = []

for tweet in tweepy.Cursor(api.search,q="#bugbountytip",count=1000,
                           lang="en",
                           since="2019-01-01",tweet_mode="extended").items():
    if hasattr(tweet, 'retweeted_status'):
        tweets.append(tweet.retweeted_status.id)

    else:
        tweets.append(tweet.id)
        print(tweet.user.id)
        print(tweet.id)
        print(tweet.created_at)
        print(tweet.user.name)
        print(tweet.user.screen_name)
        print(tweet.retweet_count)
        print(tweet.favorite_count)
        print(tweet.user.profile_image_url)
        print(tweet.full_text)
        print("\n")

        db=MySQLdb.connect(user="root",passwd="localhost",db="bugbountytip",use_unicode=True, charset="utf8mb4")
        cursor=db.cursor()

        val = (tweet.user.id, tweet.id, tweet.created_at, tweet.user.name, tweet.user.screen_name, tweet.retweet_count, tweet.favorite_count, tweet.user.profile_image_url, tweet.full_text)
        sql = """INSERT IGNORE INTO tweets (author_id, tweet_id, created_at, author_name, author_screen_name, tweet_retweet_count, tweet_favorite_count, author_profile_image_url, tweet_full_text) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql,val) # TODO: use cursor.executemany(sql, val) instead val = [("a","b"), ("c","d")]
        db.commit()

        #print (tweet, "\n\n\n\n")


# uniq_tweets = set(tweets)

# db=MySQLdb.connect(user="root",passwd="localhost",db="bugbountytip",use_unicode=True, charset="utf8mb4")
# cursor=db.cursor()

# for tweet_id in uniq_tweets:


#     url = 'https://publish.twitter.com/oembed?url=https%3A%2F%2Ftwitter.com%2Fvavkamil%2Fstatus%2F'+str(tweet_id)
#     oembed = urllib.request.urlopen(url)


    
#     oembed_tweet = json.loads(oembed.read().decode('utf-8'))
#     print (oembed_tweet)
#     # print("Tweet ID", tweet_id)
#     # print ("URL", oembed_tweet['url'])
#     # print ("Author_name", oembed_tweet['author_name'])
#     # print ("Author_url", oembed_tweet['author_url'])
#     # print ("html", oembed_tweet['html'])
#     # print("\n")

#     tweet_id    = tweet_id
#     tweet_url   = oembed_tweet['url']
#     author_name = oembed_tweet['author_name']
#     author_url  = oembed_tweet['author_url']
#     html        = oembed_tweet['html'][:-1]

#     val = (tweet_id, tweet_url, author_name, author_url, html)
#     sql = """INSERT INTO tweets (tweet_id, tweet_url, author_name, author_url, html) VALUES (%s, %s, %s, %s, %s)"""
#     cursor.execute(sql,val) # TODO: use cursor.executemany(sql, val) instead val = [("a","b"), ("c","d")]
#     db.commit()




