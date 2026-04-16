import random

#Traingular distribution
class TriangularDistribution:
    def __init__(self, min_val, max_val, mode):
        self.min = min_val
        self.max = max_val
        self.mode = mode

    def sample(self):
        return random.triangular(self.min, self.max, self.mode)

class Inputs:
    def __init__(self):
        self.flighthours = TriangularDistribution(20.00, 80.00, 45.00)

        #Weather influence 
        def weather():
            r = random.random()

            if r < 0.60: #60%
                #Normal weather
                return 1.00
            
            elif r < 0.85: #25%
                #Bad weather
                return 0.5
            
            else: #15%
                #Good weather 
                return 1.4
        
        self.priceperminute = 32.00
        
        def additional_revenue():
            r = random.random()

            if r < 0.80: #80%
                self.additional_revenue = 0.00
            
            else: #20%
                self.additional_revenue = TriangularDistribution(2000.00, 12000.00, 5000.00)
            
            return self.additional_revenue
        
            
                
                





