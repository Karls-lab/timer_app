# calculator_model.py

class CalculatorModel:
    def __init__(self):
        self.result = 0
        self.expression_history = []


    def __make_expression_safe(self, expression):
        allowed_chars = ["0","1","2","3","4","5","6","7","8","9","^","v","*","/","+","-","(",")"]
        result = ''.join(char for char in expression if char in allowed_chars)
        return result
    

    def calculate(self, expression):
        expression = self.__make_expression_safe(expression)
        self.expression_history.append(expression)
        try:
            self.result = eval(expression)
        except:
            self.result = "Error"