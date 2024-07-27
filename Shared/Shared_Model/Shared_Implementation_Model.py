from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import zope.interface
from Shared_Interface_Model import LogisticReg
import numpy as np 
import seaborn as sns

@ zope.interface.implementer(LogisticReg)
class logisticRegression:
    def build_model(self, X, y):
        X = np.array(X)
        y = np.array(y)
        X_train,self.X_test,y_train,self.y_test=train_test_split(X, y, test_size=0.3, random_state=0)
        self.model = LogisticRegression()
        self.model.fit(X_train, y_train)

    def predict(self, x_test):
        self.X_test = x_test
        return self.model.predict(self.X_test)
    
    def classificationReport(self):
        prediction = self.model.predict(self.X_test)
        return classification_report(self.y_test, prediction)
    
    def heat_map(self):
        prediction = self.model.predict(self.X_test)
        sns.heatmap(confusion_matrix(self.y_test, prediction),annot=True,fmt="d")
        
