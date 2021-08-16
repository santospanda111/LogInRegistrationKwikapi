import pymysql

class Coordinator():

    connection = pymysql.connect(host='localhost',
                        user='san',
                        password="Santoshp123@",
                        db='UserRegistration')

    def __init__(self):

        self.cursor= self.connection.cursor()

    def get_data_by_id(self,id):
        '''This function will return the user information by using user_id'''
        get_data_query="SELECT * FROM user_data WHERE id=%s"
        self.cursor.execute(get_data_query,id)
        user= self.cursor.fetchone()
        return user

    def post_data(self,username):
        '''This function will check whether the username exists or not'''
        check_statement='SELECT EXISTS(SELECT * FROM user_data WHERE username=%s)'
        self.cursor.execute(check_statement,username)
        checked_data= self.cursor.fetchall()
        return checked_data,username

    def post_insert_data(self,first_name,last_name,email,username,password):
        '''This function will get data from server and then insert into table.
            Return: email and user_id'''

        insert_statement='INSERT INTO user_data (first_name,last_name,email,username,password) VALUES(%s,%s,%s,%s,%s)'
        insert_data=(first_name,last_name,email,username,password)
        try:
            self.cursor.execute(insert_statement,insert_data)
            self.connection.commit()
        except Exception as e:
            print(str(e))
        id_statement= "SELECT id FROM user_data WHERE username=%s"
        self.cursor.execute(id_statement,username)
        user_id=self.cursor.fetchone()
        return email,user_id

    def check_authentication(self,username,password):
        '''This method will check the username and password for authentication'''
        
        check_statement='SELECT COUNT(*) FROM user_data WHERE username=%s AND password=%s'
        check_data=(username,password)
        self.cursor.execute(check_statement,check_data)
        user=self.cursor.fetchone()
        return user