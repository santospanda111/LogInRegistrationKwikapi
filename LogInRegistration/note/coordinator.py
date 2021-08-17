from UserRegistration.coordinator import Coordinator
from log import get_logger

# Logger configuration
logger = get_logger()

class NoteCoordinator():

    def __init__(self):

        self.cursor= Coordinator().connection.cursor()

    def get_note(self,user_id):
        """
            This method is used to read data by user_id.
            :param request: It accepts user_id as parameter.
            :return: It returns the notes information by using user_id.
        """
        get_data_query="SELECT * FROM note_data WHERE user_id=%s"
        self.cursor.execute(get_data_query,user_id)
        user_note= self.cursor.fetchall()
        return user_note

    def post_note(self,user_id,title,description):
        """
            This method is used to insert data to create new note.
            :param request: It accepts user_id,title and description as parameter.
            :return: It returns True after successful insertion.
        """
        insert_query='INSERT INTO note_data (title,description,user_id) VALUES(%s,%s,%s)'
        insert_data=(title,description,user_id)
        try:
            self.cursor.execute(insert_query,insert_data)
            Coordinator().connection.commit()
        except Exception as e:
            logger.exception(e)
            print({'message':str(e)})
        return True

    def put_note(self,note_id,user_id,title,description):
        """
            This method is used to update note using note_id.
            :param request: It accepts note_id,user_id,title and description as parameter.
            :return: It returns True after successful updation.
        """
        update_query='UPDATE note_data SET title = %s, description= %s WHERE user_id = %s and note_id = %s'
        update_data=(title,description,user_id,note_id)
        self.cursor.execute(update_query,update_data)
        return True

    def delete_note(self,user_id):
        """
            This method is used to delete note using user_id.
            :param request: It accepts user_id as parameter.
            :return: It returns True after successful deletion.
        """
        delete_query='DELETE FROM note_data WHERE user_id=%s'
        self.cursor.execute(delete_query,user_id)
        return True
