#! python3
import datetime as dt
import pandas as pd
import re

''' In general the data needs to accomplish the following:
        1. Drop duplicate entries, if any
        2. Drop a row if the corresponding post_body doesn't contain a 'target' word. 
        3. Create/update a column to indicate which of these words was mentioned. (?)
'''
# One thing to note, all of the original dataframes/csv will remain intact, but new 'cleaned' csv files will be created. 

''' Class containing code that cleans all of the scraped data. '''
class DataCleaner:
    def __init__(self, target_symbols, target_names):
        self.target_symbols = target_symbols
        self.target_names = target_names
        
    ''' This is a helper function to drop any duplicated entry in the dataframe. '''
    def drop_duplicates(self, df):
        cleaned_df = df.drop_duplicates(subset=['id'], keep='first')
        return cleaned_df
    
    ''' This is a helper function to filter each dataframe based on the presence of a relevant post_body mention. '''
    def filter_dataframe(self, df):
        symbols = r'\b(?:{})\b'.format('|'.join(map(re.escape, self.target_symbols)))
        symbols_mask = df['post_body'].str.contains(symbols)
        
        names = r'\b(?:{})\b'.format('|'.join(map(re.escape, self.target_names)))
        names_mask = df['post_body'].str.contains(names)
        
        cleaned_df = df[symbols_mask | names_mask]
        return cleaned_df

    ''' Driver code to /completely/ clean each dataframe. '''
    def clean_data(self, df):
        cleaned_df = self.drop_duplicates(df)
        cleaned_df = self.filter_dataframe(cleaned_df)
        return cleaned_df