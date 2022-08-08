import psycopg2
from datetime import date
import time


class Service_me():

    """Class that defines whole service management. Object of this class is a client with arguments required to identify the
        client and make a related records """
    
    def __init__(self, first_name, last_name, car_number_plate, mileage = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.car_number_plate = car_number_plate
        self.mileage = mileage
        self.today = date.today()
    
    
    def client_init(self):
        
        """Client Identification indicates client ID, Name, Phone_number, Car brand and Car Number PLate"""
        try :
            conn = psycopg2.connect(database = 'car_service_db', user = 'postgres', password = 'datapass')
            curs = conn.cursor()
            curs.execute("""
                        SELECT * 
                        FROM clients
                        WHERE last_name = %s and car_number_plate = %s """, (self.last_name.capitalize(), self.car_number_plate.upper()))
            client_info = curs.fetchall()
            print(client_info[0:6])
        finally:
            curs.close()
            conn.close()
    
    def maintenance_plan(self):

        """List of works planned depends on mileage of a client's car"""

        try:
            conn = psycopg2.connect(database = 'car_service_db', user = 'postgres', password = 'datapass')
            curs = conn.cursor()
            curs.execute("SELECT maintenance_id, maintenance_type, maintenance_1 FROM kia")
            work_list = curs.fetchall()
            
            if self.mileage == 0 :
                time.sleep(2)
                print(f"Make sure You've entered a correct Milieage!")
            elif 17000 >= self.mileage > 0 :
                curs.execute("""
                            SELECT maintenance_id, maintenance_type, maintenance_1 
                            FROM kia 
                            WHERE maintenance_1 = 'check' or maintenance_1 = 'replacement' """)
                work_list = curs.fetchall()
                time.sleep(2)
                print('Here are all works we planning to carry out within Maintenance #1')
                time.sleep(2)
                for raw in work_list:
                    print(raw)

            elif 32000 >= self.mileage > 17000 :
                curs.execute("""
                            SELECT maintenance_id, maintenance_type, maintenance_2 
                            FROM kia 
                            WHERE maintenance_2 = 'check' or maintenance_2 = 'replacement' """)
                work_list = curs.fetchall()
                time.sleep(2)
                print('Here are all works we planning to carry out within Maintenance #2')
                time.sleep(2)
                for raw in work_list:
                    print(raw)

            elif 47000 >= self.mileage > 32000 :
                curs.execute("""
                            SELECT maintenance_id, maintenance_type, maintenance_3 
                            FROM kia 
                            WHERE maintenance_3 = 'check' or maintenance_3 = 'replacement' """)
                work_list = curs.fetchall()
                time.sleep(2)
                print('Here are all works we planning to carry out within Maintenance #3')
                time.sleep(2)
                for raw in work_list:
                    print(raw)

            elif 62000 >= self.mileage > 47000 :
                curs.execute("""
                            SELECT maintenance_id, maintenance_type, maintenance_4 
                            FROM kia 
                            WHERE maintenance_4 = 'check' or maintenance_4 = 'replacement' """)
                work_list = curs.fetchall()
                time.sleep(2)
                print('Here are all works we planning to carry out within Maintenance #4')
                time.sleep(2)
                for raw in work_list:
                    print(raw)
            
            elif 77000 >= self.mileage > 62000 :
                curs.execute("""
                            SELECT maintenance_id, maintenance_type, maintenance_5 
                            FROM kia 
                            WHERE maintenance_5 = 'check' or maintenance_5 = 'replacement' """)
                work_list = curs.fetchall()
                time.sleep(2)
                print('Here are all works we planning to carry out within Maintenance #5')
                time.sleep(2)
                for raw in work_list:
                    print(raw)

            elif 92000 >= self.mileage > 77000 :
                curs.execute("""
                            SELECT maintenance_id, maintenance_type, maintenance_6 
                            FROM kia 
                            WHERE maintenance_6 = 'check' or maintenance_6 = 'replacement' """)
                work_list = curs.fetchall()
                time.sleep(2)
                print('Here are all works we planning to carry out within Maintenance #6')
                time.sleep(2)
                for raw in work_list:
                    print(raw)
                
            elif 107000 >= self.mileage > 92000 :
                curs.execute("""
                            SELECT maintenance_id, maintenance_type, maintenance_7 
                            FROM kia 
                            WHERE maintenance_7 = 'check' or maintenance_7 = 'replacement' """)
                work_list = curs.fetchall()
                time.sleep(2)
                print('Here are all works we planning to carry out within Maintenance #7')
                time.sleep(2)
                for raw in work_list:
                    print(raw)
            
            elif 122000 >= self.mileage > 107000 :
                curs.execute("""
                            SELECT maintenance_id, maintenance_type, maintenance_8 
                            FROM kia 
                            WHERE maintenance_8 = 'check' or maintenance_8 = 'replacement' """)
                work_list = curs.fetchall()
                time.sleep(2)
                print('Here are all works we planning to carry out within Maintenance #8')
                time.sleep(2)
                for raw in work_list:
                    print(raw)
            
            elif 137000 >= self.mileage > 122000 :
                curs.execute("""
                            SELECT maintenance_id, maintenance_type, maintenance_9 
                            FROM kia 
                            WHERE maintenance_9 = 'check' or maintenance_9 = 'replacement' """)
                work_list = curs.fetchall()
                time.sleep(2)
                print('Here are all works we planning to carry out within Maintenance #9')
                time.sleep(2)
                for raw in work_list:
                    print(raw)
            
            elif 152000 >= self.mileage > 137000 :
                curs.execute("""
                            SELECT maintenance_id, maintenance_type, maintenance_10 
                            FROM kia 
                            WHERE maintenance_10 = 'check' or maintenance_10 = 'replacement' """)
                work_list = curs.fetchall()
                time.sleep(2)
                print('Here are all works we planning to carry out within Maintenance #10')
                time.sleep(2)
                for raw in work_list:
                    print(raw)
        
        finally:
            curs.close()
            conn.close()

    def maintenance_perform(self):

        """Performs maintenance with apropriate records in DataBase"""
        
        while True:

            request = str(input('Are You agree with terms of use and ready to begin the maintenance? [y/n]')).lower()
                              
            if request == 'n':
                time.sleep(2)
                print('Thank You visiting our Car Service. If You need any additional support please contact our manager.')
                break
                
            elif request == 'y':
                time.sleep(2)
                print('Thank You for choosing our Car Service. You may have a cup of tea/coffee in our lobby')
                time.sleep(2)

                
                try:
                    conn = psycopg2.connect(database = 'car_service_db', user = 'postgres', password = 'datapass')
                    curs = conn.cursor()
                    curs.execute("""
                                    UPDATE clients 
                                    SET last_mileage = '%s', service_date = %s 
                                    WHERE car_number_plate = %s""", (self.mileage, self.today, self.car_number_plate))
                    

                finally:
                    conn.commit()
                    curs.close()
                    conn.close()
                
                time.sleep(1)
                print('Maintenance is done. Data recorded in DataBase successfully!')
                break
            
            else:
                print('Please, enter a correct input. Agree[y] or Refuse[n]')
                continue



    


        
        

        