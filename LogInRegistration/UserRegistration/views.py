from .coordinator import Coordinator
import pyjq


class Index(object):
    """
    [This method will return welcome message]
    """
    def get(self)->str:
        return('Welcome to Login and Registration App')

class RegisterAPI(object):

    def get(self,pk:int)->str:
        """This method will read the data from the table."""
        try:
            id = pk
            if id is not None:
                user=Coordinator().get_data_by_id(id)
                fields=('id','first_name','last_name','email','username','password')
                if len(user)==len(fields):
                    user_dict=dict(zip(fields,user))
                user_data=pyjq.all('{first_name,last_name,email,username}', user_dict)
                return({'Data':user_data})
            return('Enter your id to get registered data')
        except Exception as e:
            return({'message':str(e)})

    def post(self,first_name:str,last_name:str,email:str,username:str,password:str)->str:
        """[This method will take the required input and register it]
        Returns:
            [returns the message if successfully registered]
        """
        try:
            get_data=Coordinator().post_data(username)
            if get_data[0][0][0]>=1:
                return({'message': 'Username is already registered with another user.'})
            get_inserted_data=Coordinator().post_insert_data(first_name,last_name,email,username,password)
            return("Registration Successful")
        except ValueError:
            return('Invalid Input') 
        except Exception as e:
            return(str(e))

class LogInAPI(object):
        
    def post(self,username:str,password:str)->str:
        """[This method will take the required input and do login]
        Returns:
            [returns the message if successfully loggedin]
        """
        try:
            user = Coordinator().check_authentication(username,password)
            if user[0]==1:
                return("Loggedin Successfully")
            return('Wrong username or password')
        except ValueError:
            return('Invalid Input') 
        except Exception:
            return("wrong credentials")