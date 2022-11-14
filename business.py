import snscrape.modules.twitter as sntwitter
import pandas as pd
from datetime import datetime

class ScrapeContent:
    
    def __init__(self, username, tweet_count):
        self.username = username
        self.tweet_count = tweet_count
    
    def scrape_content(self):
        #  list to append tweet data to
        tweets_list1 = []
        
        for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'from:{self.username}' + ' -filter:replies').get_items()):
            if i > int(self.tweet_count):
                break
            if ('@' not in tweet.content and not tweet.mentionedUsers):
                tweets_list1.append([tweet.date, tweet.id, tweet.content, tweet.user.username, tweet.retweetCount, tweet.likeCount, tweet.media])
    
        # Creating a dataframe from Creatingthe tweets list above 
        tweets_df1 = pd.DataFrame(tweets_list1, columns=['Dates', 'Tweet Id', 'Captions', 'Username', "Retweets", "Likes", "Media"])
        
        return tweets_df1.to_csv(index=False)