from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.tree import Tree

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


def stem_words(tokens):
    '''
    stemming of tokens to extract root word
    '''
    porter = PorterStemmer()
    all_stem =[]
    for token in tokens:
        stemmed = [porter.stem(word) for word in token]
        all_stem.append(stemmed)
    return(all_stem)


def get_named_entity(text):
    '''
    get NER tags for news article
    '''
    chunked = ne_chunk(pos_tag(word_tokenize(text)))
    continuous_chunk = []
    current_chunk = []     
    for i in chunked:
        if type(i) == Tree:
            current_chunk.append(" ".join([token for token, pos in i.leaves()]))
        elif current_chunk:
                named_entity = " ".join(current_chunk)
                if named_entity not in continuous_chunk:
                    continuous_chunk.append(named_entity)
                    current_chunk = []
        else:
            continue
    return (continuous_chunk)

def ner_for_paragraph(combined_excel):
    '''
    apply work_token_and_stop_word_removal function for paragraph
    '''
    ner_list=[]
    for paragraph in combined_excel['text']:
        ner = get_named_entity(paragraph)
        ner_list.append(ner)
    return (ner_list)

