from .coordinator import NoteCoordinator


class NotesAPI(object):

    def get(self, user_id:int)->str:
        """This method will read the data from the table."""
        try:
            if user_id is not None:
                all_note=[]
                user=NoteCoordinator().get_note(user_id)
                fields=('note_id','title','description','user_id')
                if len(user)!=0:
                    for note in user:
                        if len(note)==len(fields):
                            note_dict=dict(zip(fields,note))
                            all_note.append(note_dict)
                    return({'Data':all_note})
                return('Data not found')
            return('Enter your user_id to get note data')  
        except AssertionError as e:
            return("Put user id to get notes")
        except Exception as e:
            return(str(e))

    def post(self,user_id:int,title:str,description:str) -> str:
        """
            :param: title, description and user id as parameter.
            :return: It's return response that notes succcessfully created or not.
        """
        try:
            insert_data=NoteCoordinator().post_note(user_id,title,description)
            if insert_data is True:
                return('Notes created successfully')
        except KeyError:
            return('Invalid Input')
        except Exception:
            return('something went wrong')

    def put(self,note_id:int,user_id:int,title:str,description:str)->str:
        """This method is used to update the data from the table by using id and note_id as a parameter"""
        try:
            updated_data=NoteCoordinator().put_note(note_id,user_id,title,description)
            if updated_data is True:
                return('Complete Data Updated')
        except ValueError:
            return('Invalid Input')
        except Exception as e:
            return(str(e))

    def delete(self,user_id:int)->str:
        """This method is used to delete the data from the table by using id as a parameter"""
        try:
            deleted_data=NoteCoordinator().delete_note(user_id)
            if deleted_data is True:
                return('Data Deleted') 
        except ValueError:
            return('Invalid Input')
        except Exception as e:
            return(str(e))