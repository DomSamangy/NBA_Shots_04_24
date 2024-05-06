import pandas as pd
import numpy as np
import sympy as sp
import math
from sympy import oo


numerical_inf = 1.79769313e+307


class DiscreteVariableDistribution:
    def __init__(self, value: list, probability: list):
        self.value = value
        self.probability = probability
        self.value_array_length = len(value)
        self.probability_array_length = len(probability)
        self.validate_parameters()


    def validate_parameters(self):
        if self.value_array_length!= self.probability_array_length:
            raise ValueError('array lengths must be equal to each other')
        if round(sum(self.probability), 4) != 1:
            raise ValueError('probability sum must be equal to 1')

    

class DiscreteVarCharacteristics(DiscreteVariableDistribution):
    def __init__(self, value, probability):
        DiscreteVariableDistribution.__init__(self, value, probability)


    def raw_moment(self, n: int, digits_to_round: int = 2) -> float: 
        """ Returns the n-th raw moment """
        sum: float = 0
        for i in range(self.value_array_length):
            sum += self.probability[i]*self.value[i]**n   
        return round(sum, digits_to_round)


    def math_expectancy(self, digits_to_round: int = 2) -> float:
        """ Returns expectancy """
        return self.raw_moment(1, digits_to_round)


    
    def central_moment(self, n: int, digits_to_round: int = 2) -> float: 
        """ Returns the n-th central moment """
        sum: float = 0
        for i in range(self.value_array_length):
            sum += self.probability[i]*(self.value[i]-self.math_expectancy(digits_to_round))**n   
        return round(sum, digits_to_round)


    def dispersion(self, digits_to_round: int = 2) -> float:
        """ Returns dispersion """
        return self.central_moment(2, digits_to_round)


    def standard_deviation(self, digits_to_round: int): 
        """ Returns the standard deviation """
        return round(math.sqrt(self.dispersion(digits_to_round)), digits_to_round)
    
    
    def moment_generating_function(self) -> sp.core.add.Add:
        """ Returns a moment-generating function """
        t = sp.Symbol('t')
        sum = 0
        for i in range(self.value_array_length):
            sum += self.probability[i]*sp.exp(t*self.value[i])
        return sum
    
    
    def characteristic_function(self) -> sp.core.add.Add: 
        """ Returns a characteristic function """
        t = sp.Symbol('t')
        sum = 0
        for i in range(self.value_array_length):
            sum += self.probability[i]*sp.exp(sp.I*t*self.value[i])
        return sum
    
    
    def raw_moment_from_mgf(self, n: int, digits_to_round: int) -> float: 
        """ Returns the n-th raw moment by deriving the moment-generating function """
        t = sp.Symbol('t')
        mgf = self.moment_generating_function()
        der = sp.diff(mgf, t, n)
        moment = sp.lambdify(t, der)
        return round(moment(0), digits_to_round)
    
    
    def raw_moment_from_cf(self, n: int, digits_to_round: int) -> float: 
        """ Returns the n-th raw moment by deriving the characteristic function """
        t = sp.Symbol('t')
        mgf = self.characteristic_function()
        der = (sp.I**(-n))*sp.diff(mgf, t, n)
        moment = sp.lambdify(t, der)
        return round(float(sp.re(moment(0))), digits_to_round)
    
    
    def skewness(self, digits_to_round: int) -> float: 
        """ Returns skewness """
        return round(self.central_moment(3, digits_to_round)/(self.standard_deviation(digits_to_round)**3), digits_to_round)
    
    
    def kurtosis(self, digits_to_round: int) -> float: 
        """ Returns kurtosis """
        return round(self.central_moment(4, digits_to_round)/(self.standard_deviation(digits_to_round)**4), digits_to_round)


    def cdf(self) -> list[np.ndarray, list]: 
        """ Returns the values of cumulative distribution function """
        y_critical_points = []
        sum = 0
        for x in range(len(self.value)):
            sum += self.probability[x]
            y_critical_points.append(round(sum, 4))


        step = 0.1
        x_axis = np.arange(self.value[0], self.value[-1]+step, step)
        x_critical_points = self.value
        y_axis = []
        tmp = 0
        x_i = x_axis[0]
        while x_i <= x_axis[-1]:
            if x_i < x_critical_points[tmp+1]:
                y_axis.append(y_critical_points[tmp])
            else:
                tmp+=1
                y_axis.append(y_critical_points[tmp])
            x_i+=step
        y_axis[-1] = 1
        return [x_axis, y_axis]
        



class ContinuousVariableDistribution:
    def __init__(self, pdf: sp.core.add.Add, value_range: list):
        self.pdf = pdf
        self.lower_bound = value_range[0]
        self.upper_bound = value_range[1]
        self.pdf_int = sp.integrals.meijerint.meijerint_definite(self.pdf, x, self.lower_bound, self.upper_bound) 
        self.validate_parameters()
    
    
    def validate_parameters(self):
        if round(self.pdf_int[0], 4) != 1:
            raise ValueError('integral of pdf should be equal to 1 from negative infinity to positive infinity')
        tmp_lower = self.lower_bound
        tmp_higher = self.upper_bound
        if self.lower_bound == -oo:
            tmp_lower = -numerical_inf
        if self.upper_bound == oo:
            tmp_higher = numerical_inf
        for i in np.linspace(tmp_lower, tmp_higher, int(1e4)):
            pdf_i = sp.lambdify(x, self.pdf)
            if pdf_i(i) < 0:
                raise ValueError('pdf value must be non-negative')
            

class ContinuousVarCharacteristics(ContinuousVariableDistribution):
    def __init__(self, pdf: sp.core.add.Add, value_range: list):
        ContinuousVariableDistribution.__init__(self, pdf, value_range)
    
    
    def cdf(self):
        tmp = sp.integrals.meijerint.meijerint_definite(self.pdf, x, self.lower_bound, x)[0]
        func = sp.expand(tmp)
        return func
    
    
    def raw_moment(self, n: int, digits_to_round: int = 2):
        return(round(sp.integrals.meijerint.meijerint_definite(x**n * self.pdf, x, self.lower_bound, self.upper_bound)[0], digits_to_round))
    
    
    def expectancy(self, digits_to_round: int = 2):
        return self.raw_moment(1, digits_to_round)
    
    
        
        
        
        




if __name__ == '__main__':
    b, a, x = sp.symbols('b, a, x',positive=True)
    lam = 2
    exponential_distr = lam*sp.exp(-lam*x)
    tmp = ContinuousVarCharacteristics(exponential_distr, [0, oo])
    print()    
