# dddilligence
This code will eventually become a web application that allows users to browse and manipulate data related to various stocks and cryptocurrencies. 
  - The project has room for many expansions, but will begin in a more 'bare' state. 
  
  As features become implemented this README will be exapanded.
  
  Features:
  1. Scrapes ledgers for the most traded items by volume, and store various data points for each item. More specifically, things such as name, symbol (or ticker), price in USD, market cap volume, total volume, and price change (% and otherwise) are stored. 
  2. Scrape various related subreddits, storing data about the top 100 posts, sorted by 'hot'. The data stored related to things such as title, score (up versus down votes), number of comments, date of posting, and the content of the post itself.  
  3. Upload the scraped and cleaned data to a database solution such that it can be queried by a user-facing web application. 
