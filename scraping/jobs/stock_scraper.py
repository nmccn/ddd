#! python3
import datetime as dt
import requests
import pandas as pd
import lxml.html as lh

'''' Class containing the code that scrapes the stock ticker/information from various stock & crypto sites'''
class StockScraper:
    
    def __init__(self, source, stock_or_crypto):
        self.source = source
        self.stock_or_crypto = stock_or_crypto

    ''' This is a function that scrapes a table from a provided web page.'''
    def scrape_table(self):
        col = []
        i = 0
        
        url = self.source
        page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        html_doc = lh.fromstring(page.content)
        tr_elements = html_doc.xpath('//tr')

        for t in tr_elements[0]:
            i+=1
            name = t.text_content()
            col.append((name,[]))
            # print(name)
            
        for i in range(1, len(tr_elements)):
            T = tr_elements[i]
            if (len(T) != 10):
                break

            j = 0

            for t in T.iterchildren():
                data = t.text_content()
                if (i > 0):
                    try:
                        data = int(data)    
                    except:
                        pass
                col[j][1].append(data)
                j+=1

        ticker_dictionary = {title:column for (title,column) in col}
        
        ticker_dataframe = pd.DataFrame(ticker_dictionary)
        # print(ticker_dataframe)
        ticker_dataframe.to_csv('{}_ticker_dataframe_{}.csv'.format(self.stock_or_crypto, dt.datetime.now().hour), mode='a')
















