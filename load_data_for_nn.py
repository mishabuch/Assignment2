# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from abc import ABC
from scipy.io import arff
import numpy as np
from sklearn import preprocessing
import sklearn.model_selection as model_selection
import pandas as pd
from sklearn.preprocessing import StandardScaler


class DataSetLoaderBaseClass(ABC):
    def __init__(self, file_path, randomness):
        self.test_x = None
        self.test_y = None
        self.train_x = None
        self.train_y = None
        self.validation_x = None
        self.validation_y = None
        self.x = None
        self.y = None
        self.feature_names = None
        self.target_labels = None
        self.data = None
        self.dataset_name = None
        self.randomness = randomness
        self.file_path = file_path


class DiabetesDataSet(DataSetLoaderBaseClass):
    def __init__(self, split_value=0.2, file_path='datasets/diabetes/messidor_features.arff', randomness=1):
        super().__init__(file_path, randomness)
        dataset = arff.loadarff(file_path)
        df = pd.DataFrame(dataset[0])
        attributes = pd.DataFrame(dataset[1])
        self.data = df
        self.dataset_name = 'Diabetes Data Set'
        self.file_path = file_path
        self.randomness = randomness

        self.target_labels = attributes[-1:][0].to_list().pop()
        self.feature_names = attributes[0:-1][0].to_list()

        # assign x and y
        self.x = np.array(self.data.iloc[:, 0:-1])
        self.y = np.array(self.data.iloc[:, -1])

        # Standardizing data
        scaler = StandardScaler()
        self.x = scaler.fit_transform(self.x)
        self.y = self.y.astype('int')

        self.train_x, self.test_x, self.train_y, self.test_y = model_selection.train_test_split(
            self.x, self.y, test_size=split_value, random_state=self.randomness, stratify=self.y
        )
        
        self.train_x, self.validation_x, self.train_y, self.validation_y = model_selection.train_test_split(
            self.train_x, self.train_y, test_size=split_value, random_state=self.randomness, stratify=self.y
        )
        tst = pd.DataFrame(np.hstack((self.test_x,self.test_y)))
        trg = pd.DataFrame(np.hstack((self.train_x,self.train_y)))
        val = pd.DataFrame(np.hstack((self.validation_x,self.validation_y)))
        tst.to_csv('test.csv',index=False,header=False)
        trg.to_csv('train.csv',index=False,header=False)
        val.to_csv('validation.csv',index=False,header=False)


def load_datasets():
    datasetDiabetes = DiabetesDataSet()
    return datasetDiabetes