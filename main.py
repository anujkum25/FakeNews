
from article_collection import article_collection
from data_preprocessing import tokenization_for_paragraph, stem_words, ner_for_paragraph
from prepare_data_for_training import training_and_test_data
from datetime import datetime

start = datetime.now()

## uncomment to download new articles
#article_collection()

## train test split
train,test = training_and_test_data()
print(train.head(),test.head())


# preprocessing pipeline
#all_tokens= tokenization_for_paragraph(test)
#all_stem= stem_words(all_tokens)
#all_ner=ner_for_paragraph(train)

end = datetime.now()
spent=end-start
print("total time taken: ",spent)