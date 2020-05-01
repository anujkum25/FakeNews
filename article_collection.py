
from utility_functions import available_sources, paper_build, article_build, filter_articles,download_and_parse_article,store_articles, remove_article_non_english

def article_collection():
    '''
    Extract and store articles
    '''
    urls=available_sources()

    paper_list=[]
    for url in urls:
        paper= paper_build(url)
        for category in paper.category_urls():
            paper_list.append(paper)
            print(category)

    all_articles=[]
    for paper in paper_list:
        url_lists=article_build(paper)
        filtered_articles=filter_articles(url_lists)
        acceptable_articles=remove_article_non_english(filtered_articles)
        all_articles.append(acceptable_articles)

    flat_list = [item for sublist in all_articles for item in sublist]
    article_texts=download_and_parse_article(flat_list)
    store_articles(article_texts)

    return()

article_collection()