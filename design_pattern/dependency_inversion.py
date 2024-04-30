# 5. Dependency inversion principle.

# Abstractions should not depend upon details. Details should depend upon abstractions.

# app_dip.py

# without DIP
class FrontEnd:
    def __init__(self, back_end):
        self.back_end = back_end

    def display_data(self):
        data = self.back_end.get_data_from_database()
        print("Display data:", data)

class BackEnd:
    def get_data_from_database(self):
        return "Data from the database"

f = FrontEnd(BackEnd())    
f.display_data()

# With DIP.

from abc import ABC, abstractmethod

class FrontEnd:
    def __init__(self, data_source):
        self.data_source = data_source

    def display_data(self):
        data = self.data_source.get_data()
        print("Display data:", data)

class DataSource(ABC):
    @abstractmethod
    def get_data(self):
        pass

class Database(DataSource):
    def get_data(self):
        return "Data from the database"

class API(DataSource):
    def get_data(self):
        return "Data from the API"
    

# use it

db_front_end = FrontEnd(Database())
db_front_end.display_data()
#Display data: Data from the database

api_front_end = FrontEnd(API())
api_front_end.display_data()
#Display data: Data from the API