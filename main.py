import os
from article_collection import article_collection
from utility_functions import read_stored_excel_and_combine
from source_selection import path, primary_tags
from data_preprocessing import tokenization_for_paragraph, stem_words, ner_for_paragraph

## uncomment to download new articles
#article_collection()

path1=os.path.join(path, str(primary_tags[0]))
path2=os.chdir(path1)

input_df = read_stored_excel_and_combine(path2)

# selecting only a small fraction of pandas dataframe for quick processing
# and check. Also there is a bug here, it does not work for full df. to be checked
input_df1= input_df.head()

all_tokens= tokenization_for_paragraph(input_df1)
#print(all_tokens)
all_stem= stem_words(all_tokens)
#print(all_stem)
all_ner=ner_for_paragraph(input_df1)
print(all_ner)