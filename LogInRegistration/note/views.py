from .coordinator import NoteCoordinator
from log import get_logger

# Logger configuration
logger = get_logger()

class Notes(object):

    def get(self, user_id:int)->str:
        """
            This method is used to read the notes according to user.
            :param request: It accepts user_id as parameter with datatypes.
            :return: It returns the note data.
        """
        try:
            if user_id is not None:
                all_note=[]
                user=NoteCoordinator().get_note(user_id)
                fields=('note_id','title','description','user_id')
                if len(user)!=0:
                    for note in user:
                        note_dict=dict(zip(fields,note))
                        all_note.append(note_dict)
                    return({'Data':all_note})
                return({'message':'Data not found'})
            return({'message':'Enter your user_id to get note data'})  
        except AssertionError as e:
            logger.exception(e)
            return({"message":"Put user id to get notes"})
        except Exception as e:
            logger.exception(e)
            return({"message":str(e)})

    def post(self,user_id:int,title:str,description:str) -> str:
        """
            This method is used to create new notes according to user.
            :param request: It accepts user_id,title and description as parameter with datatypes.
            :return: It returns response that notes successfully created or not.
        """
        try:
            insert_data=NoteCoordinator().post_note(user_id,title,description)
            if insert_data is True:
                return({'message':'Notes created successfully'})
        except KeyError as e:
            logger.exception(e)
            return({'message':'Invalid Input'})
        except Exception as e:
            logger.exception(e)
            return({'message':'something went wrong'})

    def put(self,note_id:int,user_id:int,title:str,description:str)->str:
        """
            This method is used to update notes using note_id.
            :param request: It accepts note_id,user_id,title and description as parameter with datatypes.
            :return: It returns response that notes successfully updated or not.
        """
        try:
            update_data=NoteCoordinator().put_note(note_id,user_id,title,description)
            if update_data is True:
                return({'message':'Complete Data Updated'})
        except ValueError as e:
            logger.exception(e)
            return({'message':'Invalid Input'})
        except Exception as e:
            logger.exception(e)
            return({'message':str(e)})

    def delete(self,user_id:int)->str:
        """
            This method is used to delete notes using user_id.
            :param request: It accepts user_id as parameter with datatypes.
            :return: It returns response that notes successfully deleted or not.
        """
        try:
            delete_data=NoteCoordinator().delete_note(user_id)
            if delete_data is True:
                return({'message':'Data Deleted Successfully'}) 
        except ValueError as e:
            logger.exception(e)
            return({'message':'Invalid Input'})
        except Exception as e:
            logger.exception(e)
            return({'message':str(e)})