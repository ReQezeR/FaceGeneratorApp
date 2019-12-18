import sqlite3


class DbProvider:
    def get_data_from_table(self, table_name):
        #  Get headers of table
        header_request = '''SELECT name FROM PRAGMA_TABLE_INFO('{}')'''.format(table_name)
        self.cursor.execute(header_request)
        headers = self.cursor.fetchall()

        #  Get rows of table
        sql = '''SELECT * FROM {}'''.format(table_name)
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()

        #  Create dict
        dataset = {}
        data = {}
        j = 0
        for row in rows:
            i = 0
            for item in row:
                data[str(headers[i][0])] = str(item)
                i += 1
            dataset[str(j)] = data.copy()
            j += 1
            data.clear()
        self.dataSet.clear()
        self.dataSet = dataset
        return dataset

    def __init__(self):
        self.dataSet = {}
        # Create database if not exist and get a connection to it
        self.connection = sqlite3.connect('DatabaseBackend/db.sqlite')
        # Get a cursor to execute sql statements
        self.cursor = self.connection.cursor()

        # Create tables
        self.custom_face = self.CustomFace(self)
        self.face = self.Face(self)
        self.eyes = self.Eyes(self)
        self.nose = self.Nose(self)
        self.lips = self.Lips(self)
        self.ears = self.Ears(self)
        self.hair = self.Hair(self)
        self.AttributeAssignment = self.AttributeAssignment(self)
        self.appearance = self.Appearance(self)

    class Face:
        def insert_into_table(self, shape, size, colour, path):
            sql = '''INSERT INTO Face (Shape,Size,Colour,Path) VALUES ('{}',{},'{}','{}');'''.format(shape, size, colour, path)
            self.cursor.execute(sql)
            self.connection.commit()

        def __init__(self, parent):
            self.connection = parent.connection
            self.cursor = parent.cursor
            sql = '''CREATE TABLE IF NOT EXISTS Face
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Shape VARCHAR(100),
            Size INTEGER,
            Colour VARCHAR(100),
            Path VARCHAR(100)
            )'''
            self.cursor.execute(sql)
            self.connection.commit()

    class Eyes:
        def insert_into_table(self, shape, size, colour, path):
            sql = '''INSERT INTO Eyes (Shape, Size, Colour, Path) VALUES ('{}',{},'{}','{}');'''.format(shape, size,colour, path)
            self.cursor.execute(sql)
            self.connection.commit()

        def __init__(self, parent):
            self.connection = parent.connection
            self.cursor = parent.cursor
            sql = '''CREATE TABLE IF NOT EXISTS Eyes
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Shape VARCHAR(100),
            Size INTEGER,
            Colour VARCHAR(100),
            Path VARCHAR(100)
            )'''
            self.cursor.execute(sql)
            self.connection.commit()

    class Nose:
        def insert_into_table(self, shape, size, colour, path):
            sql = '''INSERT INTO Nose (Shape, Size, Colour, Path) VALUES ('{}',{},'{}','{}');'''.format(shape, size,colour, path)
            self.cursor.execute(sql)
            self.connection.commit()

        def __init__(self, parent):
            self.connection = parent.connection
            self.cursor = parent.cursor
            sql = '''CREATE TABLE IF NOT EXISTS Nose
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Shape VARCHAR(100),
            Size INTEGER,
            Colour VARCHAR(100),
            Path VARCHAR(100)
            )'''
            self.cursor.execute(sql)
            self.connection.commit()

    class Lips:
        def insert_into_table(self, shape, size, colour, path):
            sql = '''INSERT INTO Lips (Shape, Size, Colour, Path) VALUES ('{}',{},'{}','{}');'''.format(shape, size, colour, path)
            self.cursor.execute(sql)
            self.connection.commit()

        def __init__(self, parent):
            self.connection = parent.connection
            self.cursor = parent.cursor
            sql = '''CREATE TABLE IF NOT EXISTS Lips
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Shape VARCHAR(100),
            Size INTEGER,
            Colour VARCHAR(100),
            Path VARCHAR(100)
            )'''
            self.cursor.execute(sql)
            self.connection.commit()

    class Ears:
        def insert_into_table(self, shape, size, colour, path):
            sql = '''INSERT INTO Ears (Shape, Size, Colour, Path) VALUES ('{}',{},'{}','{}');'''.format(shape, size, colour, path)
            self.cursor.execute(sql)
            self.connection.commit()

        def __init__(self, parent):
            self.connection = parent.connection
            self.cursor = parent.cursor
            sql = '''CREATE TABLE IF NOT EXISTS Ears
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Shape VARCHAR(100),
            Size INTEGER,
            Colour VARCHAR(100),
            Path VARCHAR(100)
            )'''
            self.cursor.execute(sql)
            self.connection.commit()

    class Hair:
        def insert_into_table(self, hair_type, colour, path):
            sql = '''INSERT INTO Hair (Typ, Colour, Path) VALUES ('{}','{}','{}');'''.format(hair_type, colour, path)
            self.cursor.execute(sql)
            self.connection.commit()

        def __init__(self, parent):
            self.connection = parent.connection
            self.cursor = parent.cursor
            sql = '''CREATE TABLE IF NOT EXISTS Hair
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Typ VARCHAR(100),
            Colour VARCHAR(100),
            Path VARCHAR(100)
            )'''
            self.cursor.execute(sql)
            self.connection.commit()

    class AttributeAssignment:  # AttributeAssignment
        def insert_into_table(self, faceID, eyesID, noseID, lipsID, earsID, hairID):
            sql = '''INSERT INTO AttributeAssignment (FaceID, EyesID, NoseID, LipsID, EarsID, HairID) 
            VALUES ({},{},{},{},{},{});'''.format(faceID, eyesID, noseID, lipsID, earsID, hairID)
            self.cursor.execute(sql)
            self.connection.commit()

        def __init__(self, parent):
            self.connection = parent.connection
            self.cursor = parent.cursor
            sql = '''CREATE TABLE IF NOT EXISTS AttributeAssignment
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            FaceID INTEGER,
            EyesID INTEGER,
            NoseID INTEGER, 
            LipsID INTEGER, 
            EarsID INTEGER, 
            HairID INTEGER,
            FOREIGN KEY(FaceID) references Face(ID),
            FOREIGN KEY(EyesID) references Eyes(ID),
            FOREIGN KEY(NoseID) references Nose(ID),
            FOREIGN KEY(LipsID) references Lips(ID),
            FOREIGN KEY(EarsID) references Ears(ID),
            FOREIGN KEY(HairID) references Hair(ID)
            )'''
            self.cursor.execute(sql)
            self.connection.commit()

    class Appearance:  # Appearance
        def insert_into_table(self, assignmentID, filePath):
            sql = '''INSERT INTO Appearance (AssignmentID, Path) VALUES ({}, '{}');'''.format(assignmentID, filePath)
            self.cursor.execute(sql)
            self.connection.commit()

        def __init__(self, parent):
            self.connection = parent.connection
            self.cursor = parent.cursor
            sql = '''CREATE TABLE IF NOT EXISTS Appearance
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            AssignmentID INTEGER,
            Path varchar(100),
            FOREIGN KEY(AssignmentID) references AttributeAssignment(ID)
            )'''
            self.cursor.execute(sql)
            self.connection.commit()

    class CustomFace:
        def insert_into_table(self, name, genetic, path):
            sql = '''INSERT INTO CustomFace (Name, Genetic, Path) VALUES ('{}', '{}','{}');'''.format(name, genetic,
                                                                                                      path)
            self.cursor.execute(sql)
            self.connection.commit()

        def __init__(self, parent):
            self.connection = parent.connection
            self.cursor = parent.cursor
            sql = '''CREATE TABLE IF NOT EXISTS CustomFace
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name varchar(100),
            Genetic varchar(100),
            Path varchar(100)
            )'''
            self.cursor.execute(sql)
            self.connection.commit()


if __name__ == "__main__":
    db = DbProvider()
    # db.custom_face.insert_into_table("Hiena","Dzikie zwierze","DatabaseBackend/Files/hiena.jpg")
    # db.custom_face.insert_into_table("Lew","Dzikie zwierze","DatabaseBackend/Files/lew.jpg")
    db.get_data_from_table("CustomFace")
    # db.insert_into_table('Face', 'tempName')
    # db.get_data_from_table('Face')
