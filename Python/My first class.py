class Car:
    
    features = []
    
    def __init__(self, brand):
        self.brand = brand
        
    def addFeature(self, feature):
        self.features.append(feature)
