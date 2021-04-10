import sqlite3

class MyDHTMessage:
    def __init__(self, ID="-1", content="Error message", sender="Error", time="-1"):
        self.ID = ID
        self.content = content
        self.sender = sender
        self.time = time

    def receivemessage(self):
        pass

    def loadmessagefromDB(self, ID):
        with sqlite3.connect('..\Messages.sqlite') as sqliteconnection:
            cursor = sqliteconnection.cursor()
            cursor.execute(f"""SELECT ID, content, sender, time
                                FROM Message
                                WHERE MessageID = "{ID}" """)
            return cursor.fetchone()

    def storemessageinDB(self, content, sender, time): 
        with sqlite3.connect('..\Messages.sqlite') as sqliteconnection:
            cursor = sqliteconnection.cursor()
            cursor.execute(f"""INSERT INTO Message VALUES(Null, '{content}', '{sender}', 'time') """)
            sqliteconnection.commit()
            cursor.execute(f"SELECT COUNT(*) FROM  Message ");
            return cursor.fetchone()