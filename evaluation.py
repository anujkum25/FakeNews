import os
from simpletransformers.classification import ClassificationModel
from source_selection import saved_model_path

def evaluate_model():
    '''
    after model is trained, we use trained model to do predictions
    '''
    # within saved_model_path, there shall be multiple UUID for each model, one
    # needs to be picked and passed here.
    

    # TODO:create a function for model_args in models.py and then call that here. 
       
    model_args = {
        "use_early_stopping": True,
        "early_stopping_delta": 0.05,
        "early_stopping_metric": "mcc",
        "early_stopping_metric_minimize": False,
        "early_stopping_patience": 5,
        "evaluate_during_training_steps": 100,
        "no_cashe": True,
        "sliding_window": True
        }

    model=ClassificationModel('roberta',"outputs\\", use_cuda=False, args=model_args)
    predictions, raw_outputs = model.predict(['Coronavirus was first found in China'])

    return(predictions)

