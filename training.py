from simpletransformers.classification import ClassificationModel
import pandas as pd
import logging
from prepare_data_for_training import training_and_test_data

logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.WARNING)

train, eval = training_and_test_data()

# Create a ClassificationModel
model = ClassificationModel('roberta', 'roberta-base', use_cuda=False) # You can set class weights by using the optional weight argument

# Train the model
model.train_model(train)

# Evaluate the model
result, model_outputs, wrong_predictions = model.eval_model(eval)
print("result:", result)
print("model_outputs:", model_outputs)
print("wrong_predictions:", wrong_predictions)
