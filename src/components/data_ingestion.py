import os
import os.path as op
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformationConfig
from src.components.data_transformation import DataTransformation

@dataclass
class DataIngestionConfig:
    train_data_path: str = op.join("artifact", "train.csv")
    test_data_path: str = op.join("artifact", "test.csv")
    raw_data_path: str = op.join("artifact", "data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered data ingestion method")

        try:
            df = pd.read_csv(r"C:\Users\Mohit\Desktop\Mohit\Projects\mlproject\notebook\data\stud.csv")
            logging.info("Read dataset as a dataframe..")

            os.makedirs(op.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            
            logging.info("Normalizing column names..")
            df.rename({"race/ethnicity": "race_ethnicity"}, axis=1, inplace=True)
            df.columns = [ col.replace(" ", "_") if " " in col else col for col in df.columns]

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train test split initiated..")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Data Ingestion successful !!!")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)
        
if __name__ == "__main__":
    obj = DataIngestion()
    train_path, test_path = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_path=train_path, test_path=test_path)


