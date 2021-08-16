from UserRegistration.coordinator import Coordinator

class NoteCoordinator():

    def __init__(self):

        self.cursor= Coordinator().connection.cursor()

    def get_note(self,user_id):
        '''This function will return the notes information by using user_id'''
        get_data_query="SELECT * FROM note_data WHERE user_id=%s"
        self.cursor.execute(get_data_query,user_id)
        user_note= self.cursor.fetchall()
        return user_note

    def post_note(self,user_id,title,description):
        '''This function will get data from server and then insert into table.'''
        insert_statement='INSERT INTO note_data (title,description,user_id) VALUES(%s,%s,%s)'
        insert_data=(title,description,user_id)
        try:
            self.cursor.execute(insert_statement,insert_data)
            Coordinator().connection.commit()
        except Exception as e:
            print(str(e))
        return True

    def put_note(self,note_id,user_id,title,description):
        '''This function will get data from server and update the note'''
        update_query='UPDATE note_data SET title = %s, description= %s WHERE user_id = %s and note_id = %s'
        update_data=(title,description,user_id,note_id)
        self.cursor.execute(update_query,update_data)
        return True

    def delete_note(self,user_id):
        '''This function will delete note data according to the user_id'''
        delete_query='DELETE FROM note_data WHERE user_id=%s'
        self.cursor.execute(delete_query,user_id)
        return True
