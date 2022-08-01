import psycopg2
from Security.db_connection import db_connection


def db_get_connection(): 
    """ Connect to the PostgreSQL database server """
    db_connection()
    

class Service_me():
    
    def __init__(self, first_name, last_name, car_number_plate, mileage=0):
        self.first_name = first_name
        self.last_name = last_name
        self.car_number_plate = car_number_plate
        self.mileage = mileage

    
    def client_init(self):
        
        """Client Identification"""
        
        with conn.cursor() as curs:
            curs.execute("SELECT * FROM clients WHERE last_name = '%s' and car_number_plate = '%s' ", (self.last_name.capitalize(), self.car_number_plate.upper()))
        return curs.fetchall()
    
if __name__ == '__main__':
    customer1 = Service_me(Valentyn, Shevchenko, AA5533AA)


    


        
        

        