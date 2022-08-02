import psycopg2
from datetime import date


class Service_me():
    
    def __init__(self, first_name, last_name, car_number_plate, mileage=0):
        self.first_name = first_name
        self.last_name = last_name
        self.car_number_plate = car_number_plate
        self.mileage = mileage
    
    
    def client_init(self):
        
        """Client Identification indicates client ID, Name, Phone_number, Car brand and Car Number PLate"""

        conn = psycopg2.connect(database = 'car_service_db', user = 'postgres', password = 'datapass')
        curs = conn.cursor()
        curs.execute("SELECT * FROM clients WHERE last_name = %s and car_number_plate = %s ", (self.last_name.capitalize(), self.car_number_plate.upper()))
        client_info = curs.fetchall()
        print(client_info[0:6])
        curs.close()
        conn.close()
    
    def service_plan(self):
        conn = psycopg2.connect(database = 'car_service_db', user = 'postgres', password = 'datapass')
        curs = conn.cursor()
        curs.execute("SELECT maintenance_id, maintenance_type, maintenance_1 FROM kia")
        work_list = curs.fetchall()
        
        if self.mileage == 0 :
            print(f"Make sure You've entered a correct Milieage!")
        elif 12000 >= self.mileage > 0 :
            curs.execute("""
                        SELECT maintenance_id, maintenance_type, maintenance_1 
                        FROM kia 
                        WHERE maintenance_1 = 'check' or maintenance_1 = 'replacement' """)
            work_list = curs.fetchall()
            print('Here are all works we planning to carry out within Maintenance #1')
            for raw in work_list:
                print(raw)
                
    





if __name__ == '__main__':
    client1 = Service_me('Valentyn', 'Shevchenko', 'AA5533AA', 5000)
    client1.service_plan()



    


        
        

        