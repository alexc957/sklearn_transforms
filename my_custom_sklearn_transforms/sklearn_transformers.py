from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import LabelEncoder, StandardScaler

# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')

class StandardTransform(BaseEstimator,TransformerMixin):
    def __init__(self):
       # self.columns = columns 
        
        self.scaler = StandardScaler()
        
    
    def fit(self,X, y= None):
        #print(type(X))
        self.scaler.fit(X)
        return self
    def transform(self,X):
        
        data = self.scaler.transform(X)
        return data 
        


