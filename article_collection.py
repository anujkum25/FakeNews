
from utility_functions import available_sources, paper_build, article_build, filter_articles,download_and_parse_article,store_articles

def article_collection():
    '''
    Extract and store articles
    '''
    urls=available_sources()

    paper_list=[]
    for url in urls:
        paper= paper_build(url)
        paper_list.append(paper)

    all_articles=[]
    for paper in paper_list:
        url_lists=article_build(paper)
        filtered_articles=filter_articles(url_lists)
        all_articles.append(filtered_articles)

    flat_list = [item for sublist in all_articles for item in sublist]
    article_texts=download_and_parse_article(flat_list)
    store_articles(article_texts)

    return()

article_collection()
