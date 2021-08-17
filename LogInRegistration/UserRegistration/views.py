from .coordinator import Coordinator
import pyjq
from log import get_logger

# Logger configuration
logger = get_logger()

class Index(object):
    """
        This method is used to return a welcome message.
        :return: It returns the welcome message when homepage is get called.
    """
    def get(self)->str:
        return({'message':'Welcome to Login and Registration App'})

class Register(object):

    def get(self,pk:int)->str:

        """
            This method is used to read the data from user_data.
            :param request: It accepts pk(primary_key) as parameter with datatypes.
            :return: It returns the registered data.
        """
        try:
            id = pk
            if id is None:
                return('Enter your id to get registered data')
            user=Coordinator().get_data_by_id(id)
            fields=('id','first_name','last_name','email','username','password')
            user_dict=dict(zip(fields,user))
            user_data=pyjq.all('{first_name,last_name,email,username}', user_dict)
            return({'Data':user_data})
        except Exception as e:
            logger.exception(e)
            return({'message':str(e)})

    def post(self,first_name:str,last_name:str,email:str,username:str,password:str)->str:
        """
            This method is used to register new user.
            :param request: It accepts first_name, last_name, email, username and password as parameter with datatypes.
            :return: It returns the message if successfully registered.
        """
        try:
            get_data=Coordinator().check_username_present(username)
            if get_data[0][0][0]>=1:
                return({'message': 'Username is already registered with another user.'})
            get_inserted_data=Coordinator().post_insert_data(first_name,last_name,email,username,password)
            return({'message':"Registration Successful"})
        except ValueError as e:
            logger.exception(e)
            return({'message':'Invalid Input'}) 
        except Exception as e:
            logger.exception(e)
            return(str(e))

class LogIn(object):
        
    def post(self,username:str,password:str)->str:
        """
            This method is used for login authentication.
            :param request: It's accept username and password as parameter.
            :return: It returns the message if successfully loggedin.
        """
        try:
            user = Coordinator().check_authentication(username,password)
            if user[0]==1:
                return({'message':"Loggedin Successfully"})
            return({'message':'Wrong username or password'})
        except ValueError as e:
            logger.exception(e)
            return({'message':'Invalid Input'}) 
        except Exception as e:
            logger.exception(e)
            return({'message':"wrong credentials"})