import zope.interface as zi

class readData(zi.Interface):
    def read_csv(self, filepath):
        pass
    def read_image(self, path, folder):
        pass
    

