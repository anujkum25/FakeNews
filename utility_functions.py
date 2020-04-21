import newspaper
from newspaper import Article
import pandas as pd
import os
import uuid
from source_selection import source_name, primary_tags, path

def uuid_token():
    '''
    Generate unique ids to add it to filename
    '''
    token=uuid.uuid1()
    return(token)

def available_sources():
    '''
    This function builds a list of newspaper sources from which
    we would curate articles for creating a ground truth knowledge base
    '''
    return list(source_name)

def paper_build(url):
    '''
    this build the newspaper object from the urls choosen above
    '''
    return (newspaper.build(url))

def article_build(paper):
    '''
    This extracts all the articles from the newspaper
    '''
    vec_of_urls=[]
    for article in paper.articles:
        vec=article.url
        vec_of_urls.append(vec)
    return(vec_of_urls)

def filter_articles(url_lists):
    '''
    This filters only the articles that we are intrested into
    '''
    useful_links=[]
    for links in url_lists:
        for tag in primary_tags:
            if tag in links:
                useful_links.append(links)
                useful_links= list(dict.fromkeys(useful_links)) # dirty hack, to be changed later
    return(useful_links)


def download_and_parse_article(useful_links):
    '''
    for the links that we want to use, download the full text of article
    and store it locally
    '''
    df=[]
    for link in useful_links:
        article = Article(link)
        article.download()
        article.parse()
        text= article.text
        df.append( [link,text])
    return (df)

def store_articles(df):
    '''
    convert the output from above function to a pandas dataframe and write it
    locally on disk
    '''
    df1=pd.DataFrame(df)
    df1.columns = ['url','text'] 
    df1.to_csv(os.path.join(path,(str(uuid_token())+"_collected_articles.csv")), sep=',', header=True, index=None,mode='w') 
    return()