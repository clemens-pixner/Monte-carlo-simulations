import random
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
        self.priceperminute = 32.00
        
        def additional_revenue(self):
            r = random.random()

            if r < 0.80: #80% no additional revenue
                return 0.00
            else: #20% additional revenue 
                return TriangularDistribution(2000.00, 12000.00, 5000.00).sample()
        
        def revenue(self):
            flighthours_value = self.flighthours.sample()
            base_revenue = flighthours_value * 60 * self.priceperminute
            extra_revenue = self.additional_revenue()
            return base_revenue + extra_revenue
        
class VariableCosts:
    def __init__(self):
        self.doc = TriangularDistribution()
        self.overhaul_reserve = TriangularDistribution()

    def total_variable_costs(self, flighthours):
        doc_cost = self.doc.sample() * flighthours
        overhaul_cost = self.overhaul_reserve.sample() * flighthours
        return doc_cost, overhaul_cost

class FixedCosts:
    def __init__(self):
        self.aoc = TriangularDistribution()
        self.insurance = TriangularDistribution()
        self.salary = 5000.00
        self.admin = TriangularDistribution()

        def other(self):
            r = random.random()
            return TriangularDistribution().sample()
        
        def total_fixed_costs(self):
            return(
                self.aoc.sample()
                + self.insurance.sample()
                + (self.salary * 12)
                + self.admin.sample()
                + self.other()
            )

class Financing: 
    def __init__(self):
        self.purchase_price = None
        self.equity = None
        self.loan = self.purchase_price - self.equity
        self.duration = None
        
        def interest_rate(self):
            pass

        def monthly_payment(self):
            r = self.interest_rate() / 12
            n = self.duration * 12
            L = self.loan

            return L * (r * (1 + r)**n) / ((1 + r)**n - 1)

class Depreciation:
    def __init__(self):
        self.holding_period = None
        self.purchase_price = None
        self.residual_value = None

    def monthly_depreciation(self):
        return (self.purchase_price - self.residual_value) / (self.holding_period * 12)

class Events:
    def technical_failure():
        r = random.random()

        if r < 0.85: #85% no additional maintenance
            return 0.0
        elif r < 0.97: #12% medium maintenance
            return TriangularDistribution(5000.00, 50000.00, 15000.00).sample() 
        elif r < 0.997: #2.7 high maintenance 
            return TriangularDistribution(30000.00, 200000.00, 80000.00).sample()
        else: #0.3% medium + high maintenance
            medium = TriangularDistribution(5000.00, 50000.00, 15000.00).sample()
            high = TriangularDistribution(30000.00, 200000.00, 80000.00).sample()
            return medium + high

    def weather_demand(self):
        r = random.random()

        if r < 0.60: #60% normal weather/demand
            return 1.00
        elif r < 0.85: #25% bad weather/demand
            return 0.5
        else: #15% good weather/demand
            return 1.4