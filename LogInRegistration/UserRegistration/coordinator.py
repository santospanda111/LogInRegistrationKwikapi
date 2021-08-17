import pymysql
from log import get_logger

# Logger configuration
logger = get_logger()

class Coordinator():

    connection = pymysql.connect(host='localhost',
                        user='san',
                        password="Santoshp123@",
                        db='UserRegistration')

    def __init__(self):

        self.cursor= self.connection.cursor()

    def get_data_by_id(self,id):
        """
            This method is used to read data by id.
            :param request: It accepts id as parameter.
            :return: It returns the user information by using id.
        """
        get_data_query="SELECT * FROM user_data WHERE id=%s"
        self.cursor.execute(get_data_query,id)
        user= self.cursor.fetchone()
        return user

    def check_username_present(self,username):
        """
            This method is used to check the username is present or not.
            :param request: It accepts username as parameter.
            :return: It returns the checked_data,username.
        """
        check_user_query='SELECT EXISTS(SELECT * FROM user_data WHERE username=%s)'
        self.cursor.execute(check_user_query,username)
        checked_data= self.cursor.fetchall()
        return checked_data,username

    def post_insert_data(self,first_name,last_name,email,username,password):
        """
            This method is used to insert the data to register the user.
            :param request: It accepts first_name,last_name,email,username and password as parameter.
            :return: It returns the email,user_id.
        """
        insert_query='INSERT INTO user_data (first_name,last_name,email,username,password) VALUES(%s,%s,%s,%s,%s)'
        insert_data=(first_name,last_name,email,username,password)
        try:
            self.cursor.execute(insert_query,insert_data)
            self.connection.commit()
        except Exception as e:
            logger.exception(e)
            print({'message':str(e)})
        get_id_query= "SELECT id FROM user_data WHERE username=%s"
        self.cursor.execute(get_id_query,username)
        user_id=self.cursor.fetchone()
        return email,user_id

    def check_authentication(self,username,password):
        """
            This method is used to check authentication.
            :param request: It accepts username and password as parameter.
            :return: It returns the 1 if username and password authenticated successfully else returns 0 through auth_user.
        """        
        authentication_check_query='SELECT COUNT(*) FROM user_data WHERE username=%s AND password=%s'
        check_values=(username,password)
        self.cursor.execute(authentication_check_query,check_values)
        auth_user=self.cursor.fetchone()
        return auth_user