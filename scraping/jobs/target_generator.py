#! python3
import datetime as dt
import pandas as pd

''' Class containing code that generates the target words/n-grams to search posts for. '''
class TargetGenerator:
    list_of_names = []
    list_of_symbols = []
    
    ''' This is a function to generate a list of target words/n-grams to search for in post_body's '''
    def generate_list(self, crypto_csv, stock_csv):
        crypto_df, stock_df = pd.read_csv(crypto_csv), pd.read_csv(stock_csv)    
        
        ''' Crypto can be used 'as-is', no extra words present in the names of companies, etc. '''
        self.list_of_symbols.append(list(crypto_df['Symbol']))
        self.list_of_names.append(list(crypto_df['Name ']))
        
        ''' Stock data needs to be cleaned a little bit before it can be useful for searching. '''
        self.list_of_symbols.append(list(stock_df['Symbol']))
        stock_df['Name'] = stock_df['Name'].map(lambda x: self.remove_extra_words(x))
        self.list_of_names.append(list(stock_df['Name']))
        
        self.list_of_symbols = [symbol for sublist in self.list_of_symbols for symbol in sublist]
        self.list_of_names = [name for sublist in self.list_of_names for name in sublist]
        
        return self.list_of_symbols, self.list_of_names

        
    ''' This is a helper function that removes 'extra' words in company names to make them better fit for searching. '''    
    def remove_extra_words(self, name):
        
        words_to_remove = ['Inc.', 'Company', 'Holding', 'Holdings', 'Group', 'Corporation', 
                           'S.A', 'Limited', 'Ltd.', 'S.A', 'plc', 'p.l.c', 'The', 'Corp.', 
                           'Co.', 'S.A.', 'p.l.c.', 'Technologies', 'Incorporated', '(publ)',
                           'inc.', 'Ltd', 'Markets'] 
        
        name = name.replace(',', '')
        for word in name.split():
           if word in words_to_remove:
                name = name.replace(word, '').strip()
                name = name[:-1].strip() if name.endswith("&") else name
        return name