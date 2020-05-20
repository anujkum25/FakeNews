from simpletransformers.classification import ClassificationModel
import logging
import sklearn
import os
from prepare_data_for_training import training_and_test_data, training_and_test_data_for_ref
from source_selection import saved_model_path
from utility_functions import uuid_token
from datetime import datetime


logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.WARNING)


def most_accurate_model():
    '''
    This takes a lot of time to run as most paramters are set at ideal values.
    it may take upto several days to run.
    not recommended
    
    Returns
    -------
    result : TYPE
        DESCRIPTION.
    model_outputs : TYPE
        DESCRIPTION.
    wrong_predictions : TYPE
        DESCRIPTION.

    '''
    train, eval = training_and_test_data()
    
    model = ClassificationModel('roberta', 'roberta-base', use_cuda=False) 
    
    model.train_model(train)

    result, model_outputs, wrong_predictions = model.eval_model(eval)
    
    predictions, raw_outputs = model.predict(['Coronavirus was first found in China'])
    
    return (result, model_outputs, wrong_predictions, predictions, raw_outputs)


def standard_model():
    
    '''
    Early stopping creteria enabled so that model runs faster
    
    '''
    sub_path = str(uuid_token())
    model_args = {
    "use_early_stopping": True,
    "early_stopping_delta": 0.05,
    "early_stopping_metric": "mcc",
    "early_stopping_metric_minimize": False,
    "early_stopping_patience": 5,
    "evaluate_during_training_steps": 100,
    "no_cashe": True,
    "sliding_window": True,
    "best_model_dir" : saved_model_path/ sub_path ,
    "output_dir":saved_model_path/ sub_path
    }
    
    train, eval = training_and_test_data_for_ref()
    print("train and eval split done")
    
    ## to be changed to better approach later
    #os.chdir("C:\\Users\\i345144\\OneDrive\\Documents\\MSRUS\\Group_Project\\FakeNews\\SavedModels")
    path1=saved_model_path
    os.chdir(path1)

    #12-layer, 768-hidden, 12-heads, 125M parameters RoBERTa using the BERT-base architecture
    print("pre trained model called")
    model = ClassificationModel('roberta', 'roberta-base', use_cuda=False, args=model_args)
    print("pre-trailed model done")
    
    print("model training started")
    model.train_model(train, acc=sklearn.metrics.accuracy_score)
    print("model training finished")


    result, model_outputs, wrong_predictions = model.eval_model(eval, acc=sklearn.metrics.accuracy_score)
    print("eval finished")
    
    predictions, raw_outputs = model.predict(['Coronavirus was first found in China'])
    print("prediction finished")

    return (result, model_outputs, wrong_predictions, predictions, raw_outputs)
