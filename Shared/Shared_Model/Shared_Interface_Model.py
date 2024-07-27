import zope.interface

class LogisticReg(zope.interface.Interface):
    def build_model(self, X, y):
        pass
    def predict(self, x_test):
        pass
    def classification_report(self):
        pass
    def heat_map(self):
        pass
