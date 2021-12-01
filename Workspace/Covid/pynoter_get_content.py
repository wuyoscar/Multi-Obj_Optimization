from bs4 import BeautifulSoup 
import requests
import numpy as np 
import pandas as pd 
import  xlsxwriter
from newspaper import Article
from newspaper import ArticleException
import nltk
nltk.download('punkt')
def get_fc_news(url):
    
    try:
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()
        fc_summary = article.summary
        fc_text = article.text
        fc_title = article.title
        fc_author = article.authors
        return [fc_text, fc_summary,fc_title,fc_author]
    except ArticleException:
        return [None, None,None,None]
    except TypeError:
        return [None, None,None,None]
    except AttributeError:
        return [None, None,None,None]

clean_df = pd.read_excel('clean_poynter.xlsx').iloc[:,1:]


fc_info_list = clean_df['fc_article_report']
whole_list = []
Debug_list = []
for i in range(len(fc_info_list)): 
    whole_list.append(get_fc_news(fc_info_list[i]))
    Debug_list.append(f'{i+1} url successed')

result_df = pd.DataFrame(whole_list, columns=['fc_text','fc_summary','fc_title','fc_author'])
result_df.to_csv('content_poynter')