import psycopg2


class Service_me():
    
    def __init__(self, first_name, last_name, car_number_plate, mileage=0):
        self.first_name = first_name
        self.last_name = last_name
        self.car_number_plate = car_number_plate
        self.mileage = mileage
    
    
    def client_init(self):
        
        """Client Identification"""

        conn = psycopg2.connect(database = 'car_service_db', user = 'postgres', password = 'datapass')
        curs = conn.cursor()
        curs.execute("SELECT * FROM clients WHERE last_name = %s and car_number_plate = %s ", (self.last_name.capitalize(), self.car_number_plate.upper()))
        client_info = curs.fetchall()
        print(client_info)
        curs.close()
        conn.close()


if __name__ == '__main__':
    client1 = Service_me('Valentyn', 'Shevchenko', 'AA5533AA')
    client1.client_init()



    


        
        

        