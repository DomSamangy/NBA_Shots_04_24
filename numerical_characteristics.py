import pandas as pd
import numpy as np
import sympy as sp
import math




class DiscreteCharacteristics:
    def __init__(self, value: list, probability: list):
        self.value = value
        self.probability = probability
        self.value_array_length = len(value)
        self.probability_array_length = len(probability)
        self.validate_parameters()


    def validate_parameters(self):
        if(self.value_array_length!= self.probability_array_length):
            raise ValueError('ERROR: array lengths must be equal to each other')
        if (sum(self.probability) < 0.9999 or sum(self.probability) > 1.0001):
            raise ValueError('ERROR: probability sum must be equal to 1')

    
    def raw_moment(self, power: int): #начальный момент k-ого порядка
        sum = 0
        for i in range(self.value_array_length):
            sum += self.probability[i]*self.value[i]**power   
        return sum

    
    def math_expectancy(self, argument: list): #математическое ожидание
        sum = 0
        if (self.probability_array_length == len(argument)):
            for i in range(self.value_array_length):
                sum += self.probability[i]*argument[i] 
            return sum
        else:
            raise ValueError('ERROR: array lengths must be equal to each other')

    
    def central_moment(self, power: int): #центральный момент k-ого порядка
        sum = 0
        for i in range(self.value_array_length):
            sum += self.probability[i]*(self.value[i]-self.math_expectancy(self.value))**power   
        return sum


    def standard_deviation(self): #среднеквадратичное отклонение
        return math.sqrt(self.central_moment(2))
    
    
    def moment_generating_function(self):#производящая функция моментов
        t = sp.Symbol('t')
        sum = 0
        for i in range(self.value_array_length):
            sum += self.probability[i]*sp.exp(t*self.value[i])
        return sum
    
    
    def characteristic_function(self): #характеристическая функция 
        t = sp.Symbol('t')
        sum = 0
        for i in range(self.value_array_length):
            sum += self.probability[i]*sp.exp(sp.I*t*self.value[i])
        return sum
    
    
    def raw_moment_from_mgf(self, n: int): #начальный момент через производящую функцию моментов
        t = sp.Symbol('t')
        mgf = self.moment_generating_function()
        der = sp.diff(mgf, t, n)
        moment = sp.lambdify(t, der)
        return moment(0)
    
    
    def raw_moment_from_cf(self, n: int): #начальный момент через характеристическую функцию 
        t = sp.Symbol('t')
        mgf = self.characteristic_function()
        der = (sp.I**(-n))*sp.diff(mgf, t, n)
        moment = sp.lambdify(t, der)
        return float(sp.re(moment(0)))
        




# tmp  = DiscreteCharacteristics([1, 2, 3], [0.4, 0.1, 0.5])
# # mgf = tmp.moment_generating_function()
# # print(mgf)
# c_f = tmp.characteristic_function()
# print(c_f)
# r_m = tmp.raw_moment_from_cf(1)
# print(r_m)



