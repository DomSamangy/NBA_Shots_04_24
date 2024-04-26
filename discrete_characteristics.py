import pandas as pd
import numpy as np
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


    def standard_deviation(self): 
        return math.sqrt(self.central_moment(2))
        




# tmp  = DiscreteCharacteristics([1, 2, 3], [0.4, 0.1, 0.5])
# std = tmp.standard_deviation()
# print(std)




