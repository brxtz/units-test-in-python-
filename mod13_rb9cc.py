import unittest 

class MyExcept(Exception):
    pass

class SecondExcept(Exception):
    pass

def symbol_ex(symbol):
    if(symbol != symbol.upper()):
        raise MyExcept("NOT A VALID SYMBOL... MUST BE UPPERCASE...")
    elif(len(symbol) < 1 or len(symbol) > 7):
        raise SecondExcept("NOT A VALID SYMBOL... MUST HAVE 1-7 ALPHA CHARACTERS...")
    else:
        return True
    

def chart_ex(chart_type):
    if(int(chart_type) < 1 or int(chart_type) > 2):
        raise MyExcept("NOT A VALID CHART TYPE... MUST BE 1 OR 2...")
    else:
        return True

def time_series_ex(time_series):
    if(int(time_series) < 1 or int(time_series) > 4):
        raise MyExcept("NOT A VALID TIME SERIES... MUST BE 1-4...")
    else:
        return True

def date_ex(date):
    broken_date = date.split('-')
    if(len(date) < 10 or len(date) > 10):
        raise MyExcept("NOT A VALID DATE...")
    elif(len(broken_date[0]) != 4 or len(broken_date[1]) != 2 or len(broken_date[2]) != 2):
        raise SecondExcept("WRONG FORMAT... MUST BE YYYY-MM-DD")
    else:
        return True



class SymbolTest(unittest.TestCase):
    def setUp(self):
        print("SETUP Called...")
        self.symbol = input("Enter Stock Symbol: ")

    def test_symbol_func(self):
        #Arrange
        symbol = self.symbol 
        #Act
        with self.assertRaises(MyExcept) as context1:
            symbol_ex(symbol)
        print(context1.exception)

        with self.assertRaises(SecondExcept) as context2:
            symbol_ex(symbol)
        print(context2.exception)

    def tearDown(self):
        print("TEARDOWN Called...\n\n")

class ChartTest(unittest.TestCase):
    def setUp(self):
        print("SETUP Called...")
        self.chart_type = input("Enter Chart Type (1 or 2): ")

    def test_chart_func(self):
        #Arrange
        chart_type = self.chart_type
        #Act
        with self.assertRaises(MyExcept) as context:
            chart_ex(chart_type)
        print(context.exception)
        #Assert

    def tearDown(self):
        print("TEARDOWN Called...\n\n")
        self.chart_type = 0
    
class TimeSeriesTest(unittest.TestCase):
    def setUp(self):
        print("SETUP Called...")
        self.time_series = input("Enter Time Series (1-4): ")

    def test_timeseries_func(self):
        #Arrange
        time_series = self.time_series
        #Act
        with self.assertRaises(MyExcept) as context:
            time_series_ex(time_series)
        print(context.exception)
        
    def tearDown(self):
        print("TEARDOWN Called...\n\n")
        self.time_series = 0

class DatesTest(unittest.TestCase):
    def setUp(self):
        print("SETUP Called...")
        self.start_date = input("Enter Start Date (YYYY-MM-DD): ")
        self.end_date = input("Enter End Date (YYYY-MM-DD): ")
    def test_date_func(self):
        #Arrange
        start_date = self.start_date
        end_date = self.end_date
        #Act
        with self.assertRaises(MyExcept) as context1:
            date_ex(start_date)
            date_ex(end_date)
        print(context1.exception)
        
        with self.assertRaises(SecondExcept) as context2:
            date_ex(start_date)
            date_ex(end_date)
        print(context2.exception)
        
    def tearDown(self):
        print("TEARDOWN Called...\n\n")



if __name__ == "__main__":
    unittest.main()

