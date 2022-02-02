#! python3
from distutils.command.config import config
import praw
import pandas as pd
import datetime as dt

''' Class containing the code that scrapes any provided subreddit's 'hottest' 100 posts.'''
class SubredditScraper:
    def __init__(self, sub, limit):
        self.sub = sub
        self.limit = limit
        
        # print('Instance created with values sub: {}, lim: {}'.format(sub,limit)) 
        
    ''' This is a function that scrapes the posts from an individual subreddit and passes them to a DF.'''
    def scrape_sub(self):
        post_info_dictionary = {'title' : [],
                                'score' : [],
                                'id' : [], 
                                'url' : [],
                                'num_comments' : [],
                                'date' : [],
                                'post_body' : []}
        
        # TODO: Move to an .ini file... 
        config_file = open("bot_info.txt")
        info = []
        for line in config_file:
            info.append(line)
        reddit = praw.Reddit(client_id=info[0],
                             client_secret=info[1],
                             user_agent=info[2],
                             username=info[3],
                             password=info[4])
        sub = reddit.subreddit(self.sub)
        sub = sub.hot()
        
        for post in sub:
            if post.stickied:
                continue
            else:
                # self.scrape_replies(post)
                post_info_dictionary['title'].append(post.title)
                post_info_dictionary['score'].append(post.score)
                post_info_dictionary['id'].append(post.id)
                post_info_dictionary['url'].append(post.url)
                post_info_dictionary['num_comments'].append(post.num_comments)
                post_info_dictionary['date'].append(post.created)
                post_info_dictionary['post_body'].append(post.selftext)
            
        sub_dataframe = pd.DataFrame(post_info_dictionary)
        sub_dataframe['date'] = sub_dataframe['date'].apply(lambda x: dt.datetime.fromtimestamp(x))
        
        # print(sub_dataframe)
        sub_dataframe.to_csv('reddit_dataframe_{}.csv'.format(dt.datetime.now().hour), mode='a', index=False)

    ''' This is a function that scrapes the replies to any given post and passes them to a DF.'''
    def scrape_replies(self, post):
        reply_info_dictionary = {'score' : [],
                                'id' : [], 
                                'parent_id' : [],
                                'post_body' : []}
        
        # limit=0 -> remove all instances of "MoreCommments"
        post.comments.replace_more(limit=0)
        for comment in post.comments.list():
            if comment.stickied:
                continue
            else:    
                reply_info_dictionary['id'].append(comment.id)
                reply_info_dictionary['parent_id'].append(comment.parent_id) 
                reply_info_dictionary['post_body'].append(comment.body)
                reply_info_dictionary['score'].append(comment.score)
        
        replies_dataframe = pd.DataFrame(reply_info_dictionary)
        
        # print(replies_dataframe)
        replies_dataframe.to_csv('replies_dataframe_{}.csv'.format(dt.datetime.now().hour), mode='a', index=False)
        



        
            