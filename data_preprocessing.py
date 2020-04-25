import os
import pandas as pd
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize

def remove_punctuation(text):
    '''
    remove punctuation from text of news body
    '''
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for x in text.lower(): 
        if x in punctuations:
            text = text.replace(x, "")
    return(text)


def remove_special_characters_from_text(text):
    '''
    remove newline characters etc. from text before tokenization
    '''
    new_text = remove_punctuation(text)
    updated_text = new_text.replace('\n', ' ').replace('\r', '')
    return(updated_text)

def word_token_and_stop_word_removal(text):
    '''
    for a news article paragraph, extract all tokens and
    remove stop words
    '''
    stop_words = set(stopwords.words('english'))
    updated_text = remove_special_characters_from_text (text)
    word_tokens = word_tokenize(updated_text.lower())   
    filtered_sentence = [w for w in word_tokens if not w in stop_words] 
    return (filtered_sentence)

def tokenization_for_paragraph(combined_excel):
    '''
    apply work_token_and_stop_word_removal function for paragraph
    '''
    token_list=[]
    for paragraph in combined_excel['text']:
        token = word_token_and_stop_word_removal(paragraph)
        token_list.append(token)
    return (token_list)