import pandas as pd
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
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

    
    def raw_moment(self, power: int, digits_to_round: int): #начальный момент k-ого порядка
        sum = 0
        for i in range(self.value_array_length):
            sum += self.probability[i]*self.value[i]**power   
        return round(sum, digits_to_round)

    
    def math_expectancy(self, argument: list, digits_to_round: int): #математическое ожидание
        sum = 0
        if (self.probability_array_length == len(argument)):
            for i in range(self.value_array_length):
                sum += self.probability[i]*argument[i] 
            return round(sum, digits_to_round)
        else:
            raise ValueError('ERROR: array lengths must be equal to each other')

    
    def central_moment(self, power: int, digits_to_round: int): #центральный момент k-ого порядка
        sum = 0
        for i in range(self.value_array_length):
            sum += self.probability[i]*(self.value[i]-self.math_expectancy(self.value, digits_to_round))**power   
        sum = round(sum, digits_to_round)
        return sum


    def standard_deviation(self, digits_to_round: int): #среднеквадратичное отклонение
        return round(math.sqrt(self.central_moment(2, digits_to_round)), digits_to_round)
    
    
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
    
    
    def raw_moment_from_mgf(self, n: int, digits_to_round: int): #начальный момент через производящую функцию моментов
        t = sp.Symbol('t')
        mgf = self.moment_generating_function()
        der = sp.diff(mgf, t, n)
        moment = sp.lambdify(t, der)
        return round(moment(0), digits_to_round)
    
    
    def raw_moment_from_cf(self, n: int, digits_to_round: int): #начальный момент через характеристическую функцию 
        t = sp.Symbol('t')
        mgf = self.characteristic_function()
        der = (sp.I**(-n))*sp.diff(mgf, t, n)
        moment = sp.lambdify(t, der)
        return round(float(sp.re(moment(0))), digits_to_round)
    
    
    def skewness(self, digits_to_round: int): #коэффициент асимметрии
        return round(self.central_moment(3, digits_to_round)/(self.standard_deviation(digits_to_round)**3), digits_to_round)
    
    
    def kurtosis(self, digits_to_round: int): #коэффициент экцесса
        return round(self.central_moment(4, digits_to_round)/(self.standard_deviation(digits_to_round)**4), digits_to_round)


    def cdf(self): #функция распределения
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
        




    

        

        
        

# tmp = DiscreteCharacteristics([1, 2, 3], [0.1, 0.6, 0.3])
# cdf = tmp.cdf()
# print(cdf)


