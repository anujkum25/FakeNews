from pathlib import Path

## Add all the trusted source which we want to build the knowledge base from

source_name = [
    'https://indianexpress.com/',
    'https://timesofindia.indiatimes.com/',
    'https://www.hindustantimes.com/',
    "https://www.deccanherald.com/",
    "https://www.newindianexpress.com/",
    "https://www.thehindu.com/"

]




## list of keywords for which we want to build the knowledge base
primary_tags = [
    'coronavirus',
    'covid-19',
    'corona',
    'virus'

]



secondry_tags= [
    'India',
    'Mumbai'
]



Daterange= []

## Path to store curated articles and text
#path=Path("./Data/")
path=Path("C:\\Users\\i345144\\OneDrive\\Documents\\MSRUS\\Group_Project\\FakeNews\\Data\\")
# to be changed to relative path
test_data_path=Path("C:\\Users\\i345144\\OneDrive\\Documents\\MSRUS\\Group_Project\\FakeNews\\Data\\TestData")

## saved model path
saved_model_path=Path("C:\\Users\\i345144\\OneDrive\\Documents\\MSRUS\\Group_Project\\FakeNews\\SavedModelPath")