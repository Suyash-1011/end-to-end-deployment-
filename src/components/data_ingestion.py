import os 
import sys 
from src.exception import CustomException
from src.logger import logging 
import pandas as pd 
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join("artefacts","train.csv")
    test_data_path=os.path.join("artefacts","test.csv")
    raw_data_path=os.path.join("artefacts","data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def Initiate_data_ingestion(self):
        logging.info("entered data ingestion method")
        try:
            df=pd.read_csv("notebook/data/Stud.csv")
            logging.info("read data as dataframe")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            
            logging.info("Train test split initiated")
            train_set, test_set=train_test_split(df,test_size=0.2, random_state=7)
            #Saving the train and test csv to their designated paths 
            train_set.to_csv(self.ingestion_config.train_data_path,index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Data Ingestion completed")

            return( 
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path   
            )
        except Exception as e:
            raise CustomException(e,sys)
        

if __name__=="__main__":
    obj=DataIngestion()
    obj.Initiate_data_ingestion()




