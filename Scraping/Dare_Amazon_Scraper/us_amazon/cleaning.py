import pandas as pd
from lxml.html import fromstring
from lxml.html import tostring
import os


df = pd.read_csv('data.csv')
df.columns = ['Product Title', 'ASIN', 'Price', 'Rating Count', 'Rating Out of 5', 'Category Rank', 'Comments', 'Product Descriptions', 'Featured Bulletpoints', 'Sub Category Ranking']


#Title
df['Product Title'] = df['Product Title'].astype(str).str.replace("\n", "")
df['Product Title'] = df['Product Title'].astype(str).str.replace("<span id=", "")
df['Product Title'] = df['Product Title'].astype(str).str.replace("class=", '')
df['Product Title'] = df['Product Title'].astype(str).str.replace("productTitle", '')
df['Product Title'] = df['Product Title'].astype(str).str.replace("a-size-large product-title-word-break", '')
df['Product Title'] = df['Product Title'].astype(str).str.replace('""', '')
df['Product Title'] = df['Product Title'].astype(str).str.replace('</span>', '')





#ASIN
df['ASIN'] = df['ASIN'].astype(str).str.replace('<td class="a-size-base">', "")
df['ASIN'] = df['ASIN'].astype(str).str.replace('\n', "")
df['ASIN'] = df['ASIN'].astype(str).str.replace('</td>', "")
#print(df['ASIN'])

#price
df['Price'] = df['Price'].astype(str).str.replace('\n', '')
df['Price'] = df['Price'].astype(str).str.replace("span id=", '')
df['Price'] = df['Price'].astype(str).str.replace("priceblock_ourprice", '')
df['Price'] = df['Price'].astype(str).str.replace("class=", '')
df['Price'] = df['Price'].astype(str).str.replace("a-size-medium a-color-price priceBlockBuyingPriceString", '')
df['Price'] = df['Price'].astype(str).str.replace('""','')
df['Price'] = df['Price'].astype(str).str.replace('</span>', '')
df['Price'] = df['Price'].astype(str).str.replace('NaN', 'Not Available')
df['Price'] = df['Price'].astype(str).str.replace('< >', '')

#print(df['Price'])

#Rating count 
df['Rating Count'] = df['Rating Count'].astype(str).str.replace('\n', "")

#print(df['Rating Count']) 

#Rating
#THIS IS DONE

#Category rank

df['Category Rank'] = df['Category Rank'].astype(str).str.replace('<span>', '')
df['Category Rank'] = df['Category Rank'].astype(str).str.replace('<br>', '')
df['Category Rank'] = df['Category Rank'].astype(str).str.replace('</a>', '')
df['Category Rank'] = df['Category Rank'].astype(str).str.replace('&amp;', '')
df['Category Rank'] = df['Category Rank'].astype(str).str.replace('(<a href="/gp/bestsellers/grocery/ref=pd_zg_ts_grocery">See Top 100 in Grocery  Gourmet Food)</span>', '')
df['Category Rank'] = df['Category Rank'].astype(str).str.replace(',', '')


#print(df['Category Rank'])


#Comment
#df['Comments'] = df['Comments'].str.replace('\n', '')
#print(df['Comments'])

#Product Description
df['Product Descriptions'] = df['Product Descriptions'].astype(str).str.replace('<p>', '')
df['Product Descriptions'] = df['Product Descriptions'].astype(str).str.replace('</p>', '')
df['Product Descriptions'] = df['Product Descriptions'].astype(str).str.replace('<\n', '')


#print(df['Product Descriptions'])

#Featured Bullets
'''
df['Featured Bulletpoints'] = df['Featured Bulletpoints'].str.replace('<div id="feature-bullets" class="a-section a-spacing-medium a-spacing-top-small\n', '')
df['Featured Bulletpoints'] = df['Featured Bulletpoints'].str.replace('\n', ' ')
df['Featured Bulletpoints'] = df['Featured Bulletpoints'].str.replace(' ', '\n')
df['Featured Bulletpoints'] = df['Featured Bulletpoints'].str.replace('<ul class="a-unordered-list a-vertical a-spacing-mini', '')
df['Featured Bulletpoints'] = df['Featured Bulletpoints'].str.replace('<li><span class="a-list-item">', '')
df['Featured Bulletpoints'] = df['Featured Bulletpoints'].str.replace('</span></li>', '')
df['Featured Bulletpoints'] = df['Featured Bulletpoints'].str.replace('</ul>', '')
df['Featured Bulletpoints'] = df['Featured Bulletpoints'].str.replace('<!--  Loading EDP related metadata -->', '')
df['Featured Bulletpoints'] = df['Featured Bulletpoints'].str.replace('<span class="caretnext"></span>', '')
df['Featured Bulletpoints'] = df['Featured Bulletpoints'].str.replace('<a id="seeMoreDetailsLink" class="a-link-normal" href="#productDetails">See more product details</a>', '')
df['Featured Bulletpoints'] = df['Featured Bulletpoints'].str.replace('</div>', '')
df['Featured Bulletpoints'] = df['Featured Bulletpoints'].str.replace('', '')
'''


#subcat
df['Sub Category Ranking'] = df['Sub Category Ranking'].astype(str).str.replace(',','')

df.to_excel('Data_us_clean.xlsx')

os.system('rm -r /Users/user9231/desktop/code/scraping/dare_amazon_scraper/dare_amazon_scraper/data.csv')
# put into CSV
