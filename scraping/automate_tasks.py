import datetime as dt
import pandas as pd
import shutil
from .jobs.subreddit_scraper import SubredditScraper
from .jobs.stock_scraper import StockScraper
from .jobs.data_cleaner import DataCleaner
from .jobs.target_generator import TargetGenerator
from scraping.models import RedditPostData, RedditReplyData


''' Helper function that uploads a JSON structure to an SQLite database. '''
def upload_dataframes(cleaned_csv, model_type):
    temp_df = pd.read_csv(cleaned_csv, sep=',')
    if model_type.lower() == 'post':
        objs = [
            RedditPostData(
                # title,score,id,url,num_comments,date,post_body
                title = temp_df.iloc[i]['title'],
                score = temp_df.iloc[i]['score'],
                post_id = temp_df.iloc[i]['id'],
                url = temp_df.iloc[i]['url'],
                num_comments = temp_df.iloc[i]['num_comments'],
                date = temp_df.iloc[i]['date'],
                post_body = temp_df.iloc[i]['post_body'],
        ) for i in range(len(temp_df))]
        RedditPostData.objects.bulk_create(objs)
    elif model_type.lower() == 'reply':
        for entry in cleaned_csv:
            RedditReplyData.objects.create(
                score = entry['score'],
                post_id = entry['post_id'],
                parent_id = entry['parent_id'],
                post_body = entry['post_body'],
            )
    else:
        print('Invalid type of model, will not proceed.')

''' Driver code to automate data collection, cleaning, and upload. '''
def automate_tasks():
    list_of_subreddits = ['wallstreetbets', 'CryptoCurrency', 'CryptoMarkets', 'stocks', 'pennystocks', 'investing']
    list_of_websites = ['https://www.investing.com/crypto/currencies', 'https://finance.yahoo.com/most-active/?count=200&offset=0']
    list_of_parameters = ['crypto', 'stocks']
    timestamp = dt.datetime.now().hour
    try:
        ''' Web Scraping. '''
        for site, param in zip(list_of_websites, list_of_parameters):
            StockScraper(site, param).scrape_table() 
        print('NYSE and crypto exchange sites scraped...')

        for sub in list_of_subreddits:
            SubredditScraper(sub, limit=999).scrape_sub()
        print('Various subreddits scraped...')
            
        ''' Target Generating '''
        generator = TargetGenerator() 
        target_symbols, target_names = generator.generate_list(crypto_csv='crypto_ticker_dataframe_{}.csv'.format(timestamp), stock_csv='stocks_ticker_dataframe_{}.csv'.format(timestamp))
        print('Targets generated...')
        
        ''' Data Cleaning ''' 
        cleaner = DataCleaner(target_symbols=target_symbols, target_names=target_names)

        post_df = pd.read_csv('reddit_dataframe_{}.csv'.format(timestamp))
        cleaned_post_df = cleaner.clean_data(post_df)
        cleaned_post_df.to_csv('cleaned_post_dataframe_{}.csv'.format(timestamp), index=False)
        # replies_df = pd.read_csv('replies_dataframe_{}.csv'.format(timestamp))
        # cleaned_replies_df = cleaner.clean_data(replies_df)
        # cleaned_replies_df.to_csv('cleaned_replies_dataframe_{}.csv'.format(timestamp), index=False)
        print('Data cleaned...')
        
        ''' Upload Cleaned Structures to Database '''
        # TODO
        upload_dataframes('cleaned_post_dataframe_{}.csv'.format(timestamp), 'post')
        # upload_dataframes(cleaned_replies_df.to_json(), 'reply')
        print('Cleaned data uploaded to DB...')
        
        ''' Maintaining File Structure '''
        shutil.move(src='reddit_dataframe_{}.csv'.format(timestamp), dst='old_data/')
        # shutil.move(src='replies_dataframe_{}.csv'.format(timestamp), dst='old_data/')
        shutil.move(src='stocks_ticker_dataframe_{}.csv'.format(timestamp), dst='old_data/')
        shutil.move(src='crypto_ticker_dataframe_{}.csv'.format(timestamp), dst='old_data/')
        print('Scraped files moved...')
        
    except Exception as e:
        print('The automation script failed. Usually related to the acquisition of scraped data, read the exception:')
        print(e)