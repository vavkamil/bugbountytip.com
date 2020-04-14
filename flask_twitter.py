#!/usr/bin/python

from flask import Flask, render_template
import pymysql

app = Flask(__name__)

class Database:
    def __init__(self):
        host = "127.0.0.1"
        user = "xxx"
        password = "xxx"
        db = "bugbountytip"

        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cur = self.con.cursor()

    def list_tweets(self):
        self.cur.execute("SELECT author_id, tweet_id, created_at, author_name, author_screen_name, tweet_retweet_count, tweet_favorite_count, author_profile_image_url, tweet_full_text FROM tweets ORDER BY created_at DESC")
        result = self.cur.fetchall()

        return result

    def count_tweets(self):
        self.cur.execute("SELECT count(tweet_id) FROM tweets")
        result = self.cur.fetchone()

        return result

@app.route('/')
def tweets():

    def db_query():
        db = Database()
        emps = db.list_tweets()

        return emps

    res = db_query()
    #print(res)

    def db_query2():
        db = Database()
        emps = db.count_tweets()

        return emps

    res2 = db_query2()
    #print(res)

    return render_template('tweets.html', result=res, count=res2, content_type='application/json')
