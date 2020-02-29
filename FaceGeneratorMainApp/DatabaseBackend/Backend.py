import os
import re
import sqlite3
import sys
import random


class DbProvider:
    def random_features(self, skintype):
        feature_list = {}

        def face():
            face = self.custom_select("SELECT * FROM Face e WHERE e.SkinType=LOWER('{}')".format(skintype))
            number = random.randint(1, face.__len__())
            path = face['{}'.format(number-1)]['Path']
            feature_list['face'] = path
            return number

        FaceID = face()

        def mouth():
            mouth = self.custom_select("SELECT * FROM Mouth e WHERE e.SkinType=LOWER('{}')".format(skintype))
            number = random.randint(1, mouth.__len__())
            path = mouth['{}'.format(number-1)]['Path']
            feature_list['mouth'] = path
            return number

        MouthID = mouth()

        def nose():
            nose = self.custom_select("SELECT * FROM Nose e WHERE e.SkinType=LOWER('{}')".format(skintype))
            number = random.randint(1, nose.__len__())
            nose_path = nose['{}'.format(number-1)]['Path']
            feature_list['nose'] = nose_path
            return number

        NoseID = nose()

        def eyebrows():
            eyebrows = self.custom_select(
                "SELECT L_ID, R_ID FROM EyeBrows e WHERE e.SkinType=LOWER('{}')".format(skintype))
            number = random.randint(1, eyebrows.__len__())
            l_id = eyebrows['{}'.format(number-1)]['L_ID']
            r_id = eyebrows['{}'.format(number-1)]['R_ID']
            l_eyebrow = self.custom_select("SELECT Path FROM EyeBrow e WHERE e.ID = {}".format(l_id))['0']['Path']
            r_eyebrow = self.custom_select("SELECT Path FROM EyeBrow e WHERE e.ID = {}".format(r_id))['0']['Path']
            feature_list['l_eyebrow'] = l_eyebrow
            feature_list['r_eyebrow'] = r_eyebrow
            return number

        EyeBrowsID = eyebrows()

        def eyes():
            eyes = self.custom_select("SELECT L_ID, R_ID FROM Eyes e WHERE e.SkinType=LOWER('{}')".format(skintype))
            number = random.randint(1, eyes.__len__())
            l_id = eyes['{}'.format(number-1)]['L_ID']
            r_id = eyes['{}'.format(number-1)]['R_ID']
            l_eye = self.custom_select("SELECT Path FROM Eye e WHERE e.ID = {}".format(l_id))['0']['Path']
            r_eye = self.custom_select("SELECT Path FROM Eye e WHERE e.ID = {}".format(r_id))['0']['Path']
            feature_list['l_eye'] = l_eye
            feature_list['r_eye'] = r_eye
            return number

        EyesID = eyes()

        def ears():
            ears = self.custom_select("SELECT L_ID, R_ID FROM Ears e WHERE e.SkinType=LOWER('{}')".format(skintype))
            number = random.randint(1, ears.__len__())
            l_id = ears['{}'.format(number-1)]['L_ID']
            r_id = ears['{}'.format(number-1)]['R_ID']
            l_ear = self.custom_select("SELECT Path FROM Ear e WHERE e.ID = {}".format(l_id))['0']['Path']
            r_ear = self.custom_select("SELECT Path FROM Ear e WHERE e.ID = {}".format(r_id))['0']['Path']
            feature_list['l_ear'] = l_ear
            feature_list['r_ear'] = r_ear
            return number

        EarsID = ears()

        def hair():
            hair = self.custom_select("SELECT * FROM Hair e WHERE e.SkinType=LOWER('{}')".format(skintype))
            number = random.randint(1, hair.__len__())
            path = hair['{}'.format(number-1)]['Path']
            feature_list['hair'] = path
            return number

        HairID = hair()

        id = self.addAttributeAssignment(FaceID, EyesID, EyeBrowsID, NoseID, MouthID, EarsID, HairID)
        return (id, feature_list)

    def addEyes(self, size, color, skintype, legacy):
        self.eye.insert_into_table(size, color, skintype, "left", "Files/Features/" + legacy + "/l_eye.png", legacy)
        self.eye.insert_into_table(size, color, skintype, "right", "Files/Features/" + legacy + "/r_eye.png", legacy)
        leftEye = \
            self.custom_select("SELECT ID FROM Eye e WHERE e.Side=LOWER('left') AND e.Legacy='{}'".format(legacy))[
                '0'].get(
                'ID')
        rightEye = \
            self.custom_select("SELECT ID FROM Eye e WHERE e.Side=LOWER('right') AND e.Legacy='{}'".format(legacy))[
                '0'].get('ID')
        self.eyes.insert_into_table(skintype, leftEye, rightEye)

    def addEars(self, size, skintype, legacy):
        self.ear.insert_into_table(size, skintype, "left", "Files/Features/" + legacy + "/l_ear.png", legacy)
        self.ear.insert_into_table(size, skintype, "right", "Files/Features/" + legacy + "/r_ear.png", legacy)
        leftEar = \
            self.custom_select(
                "SELECT ID FROM Ear e WHERE e.Side=LOWER('left') AND e.Legacy='{}'".format(legacy))['0'].get('ID')
        rightEar = \
            self.custom_select(
                "SELECT ID FROM Ear e WHERE e.Side=LOWER('right') AND e.Legacy='{}'".format(legacy))[
                '0'].get('ID')
        self.ears.insert_into_table(skintype, leftEar, rightEar)

    def addEyeBrows(self, size, color, skintype, legacy):
        self.eyeBrow.insert_into_table(size, color, skintype, "left", "Files/Features/" + legacy + "/l_eyebrow.png",
                                       legacy)
        self.eyeBrow.insert_into_table(size, color, skintype, "right", "Files/Features/" + legacy + "/r_eyebrow.png",
                                       legacy)
        leftEyeBrow = self.custom_select(
            "SELECT ID FROM EyeBrow e WHERE e.Side=LOWER('left') AND e.Legacy='{}'".format(legacy))['0'].get(
            'ID')
        rightEyeBrow = self.custom_select(
            "SELECT ID FROM EyeBrow e WHERE e.Side=LOWER('right') AND e.Legacy='{}'".format(legacy))['0'].get(
            'ID')
        self.eyeBrows.insert_into_table(skintype, leftEyeBrow, rightEyeBrow)

    def addNose(self, size, skintype, legacy):
        self.nose.insert_into_table(size, skintype, "Files/Features/" + legacy + "/nose.png")

    def addMouth(self, size, skintype, legacy):
        self.mouth.insert_into_table(size, skintype,"Files/Features/" + legacy + "/mouth.png")

    def addHair(self, hairtype, colour, skintype, legacy):
        self.hair.insert_into_table(hairtype, colour, skintype, "Files/Features/" + legacy + "/hair.png")

    def addFace(self, skintype, size, legacy):
        self.face.insert_into_table(skintype, size, "Files/Features/" + legacy + "/face.png")

    def addAttributeAssignment(self, faceID, eyesID, eyebrowsID, noseID, mouthID, earsID, hairID):
        self.AttributeAssignment.insert_into_table(faceID, eyesID, eyebrowsID, noseID, mouthID, earsID, hairID)
        attribiteAssignmentID = self.custom_select("SELECT ID FROM AttributeAssignment ORDER BY ID DESC LIMIT 1;")[
            '0'].get('ID')
        return attribiteAssignmentID

    def addAppearance(self, attributeAssignmentID, skintype, filePath):
        self.appearance.insert_into_table(attributeAssignmentID, skintype, filePath)

    def database_path(self, relative):
        p = os.path.join(os.environ.get("_MEIPASS2", os.path.abspath(".")), relative)
        return p

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
        self.path = self.database_path('DB/db.sqlite')
        self.dataSet = {}

        if not os.path.isfile(self.path):
            try:
                os.mkdir(self.database_path("DB"))
            except:
                pass
        # Create database if not exist and get a connection to it
        self.connection = sqlite3.connect(self.path)
        # Get a cursor to execute sql statements
        self.cursor = self.connection.cursor()

        # Create tables
        self.face = self.Face(self)
        self.eye = self.Eye(self)
        self.eyes = self.Eyes(self)
        self.ear = self.Ear(self)
        self.ears = self.Ears(self)
        self.eyeBrow = self.EyeBrow(self)
        self.eyeBrows = self.EyeBrows(self)
        self.nose = self.Nose(self)
        self.mouth = self.Mouth(self)
        self.hair = self.Hair(self)
        self.AttributeAssignment = self.AttributeAssignment(self)
        self.appearance = self.Appearance(self)

    def get_dict(self, headers, rows):  # Create dict
        dataset = {}
        data = {}
        j = 0
        for row in rows:
            i = 0
            for item in row:
                data[str(headers[i])] = str(item)
                i += 1
            dataset[str(j)] = data.copy()
            j += 1
            data.clear()
        self.dataSet.clear()
        self.dataSet = dataset
        return dataset

    def custom_select(self, select_formula):
        headers = []
        x = re.split("(?i)FROM", select_formula)
        headers = re.findall(r'(\w+)+', re.split("(?i)SELECT", x[0])[1], re.IGNORECASE)
        if headers == []:
            headers = re.findall(r'([*]+)', re.split("(?i)SELECT", x[0])[1], re.IGNORECASE)

        table_name = re.findall(r'(\w+)+', x[1], re.IGNORECASE)[0]
        # Get headers of table
        if (headers[0] == '*'):
            header_request = '''SELECT name FROM PRAGMA_TABLE_INFO('{}')'''.format(table_name)
            self.cursor.execute(header_request)
            headers = self.cursor.fetchall()
            new_headers = []
            for h in headers:
                new_headers.append(h[0])
            headers = new_headers
        #  Get rows of table
        sql = select_formula
        try:
            self.cursor.execute(sql)
        except:
            pass
        rows = self.cursor.fetchall()
        return self.get_dict(headers, rows)

    class Face:
        def insert_into_table(self, skintype, size, path):
            sql = '''INSERT INTO Face (SkinType, Size, Path) VALUES ('{}','{}','{}');'''.format(skintype, size, path)
            self.cursor.execute(sql)
            self.connection.commit()

        def __init__(self, parent):
            self.connection = parent.connection
            self.cursor = parent.cursor
            sql = '''CREATE TABLE IF NOT EXISTS Face
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            SkinType VARCHAR(100),
            Size VARCHAR(20),
            Path VARCHAR(300)
            )'''
            self.cursor.execute(sql)
            self.connection.commit()

    class Eyes:
        def insert_into_table(self, skintype, L_ID, R_ID):
            sql = '''INSERT INTO Eyes (SkinType, L_ID, R_ID) VALUES ('{}',{},{});'''.format(skintype, L_ID, R_ID)
            self.cursor.execute(sql)
            self.connection.commit()

        def __init__(self, parent):
            self.connection = parent.connection
            self.cursor = parent.cursor
            sql = '''CREATE TABLE IF NOT EXISTS Eyes
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            SkinType VARCHAR(100),
            L_ID INT,
            R_ID INT,
            FOREIGN KEY(L_ID) references Eye(ID),
            FOREIGN KEY(R_ID) references Eye(ID)
            )'''
            self.cursor.execute(sql)
            self.connection.commit()

    class Eye:
        def insert_into_table(self, size, colour, skintype, side, path, legacy):
            sql = '''INSERT INTO Eye (Size, Colour, SkinType, Side, Path, Legacy) VALUES ('{}', '{}' ,'{}','{}','{}','{}');'''.format(
                size, colour, skintype, side, path, legacy)
            self.cursor.execute(sql)
            self.connection.commit()

        def __init__(self, parent):
            self.connection = parent.connection
            self.cursor = parent.cursor
            sql = '''CREATE TABLE IF NOT EXISTS Eye
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Size VARCHAR(100),
            Colour VARCHAR(100),
            SkinType VARCHAR(100),
            Side VARCHAR(100),
            Path VARCHAR(300),
            Legacy VARCHAR(100)
            )'''
            self.cursor.execute(sql)
            self.connection.commit()

    class Nose:
        def insert_into_table(self, size, skintype, path):
            sql = '''INSERT INTO Nose (Size,SkinType,Path) VALUES ('{}','{}','{}');'''.format(size, skintype, path)
            self.cursor.execute(sql)
            self.connection.commit()

        def __init__(self, parent):
            self.connection = parent.connection
            self.cursor = parent.cursor
            sql = '''CREATE TABLE IF NOT EXISTS Nose
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Size VARCHAR(100),
            SkinType VARCHAR(100),
            Path VARCHAR(300)
            )'''
            self.cursor.execute(sql)
            self.connection.commit()

    class Mouth:
        def insert_into_table(self, size, skintype, path):
            sql = '''INSERT INTO Mouth (SkinType, Size, Path) VALUES ('{}','{}','{}');'''.format(skintype, size, path)
            self.cursor.execute(sql)
            self.connection.commit()

        def __init__(self, parent):
            self.connection = parent.connection
            self.cursor = parent.cursor
            sql = '''CREATE TABLE IF NOT EXISTS Mouth
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            SkinType VARCHAR(100),
            Size VARCHAR(100),
            Path VARCHAR(300)
            )'''
            self.cursor.execute(sql)
            self.connection.commit()

    class Ears:
        def insert_into_table(self, skintype, L_ID, R_ID):
            sql = '''INSERT INTO Ears (SkinType, L_ID, R_ID) VALUES ('{}',{},{});'''.format(skintype, L_ID, R_ID)
            self.cursor.execute(sql)
            self.connection.commit()

        def __init__(self, parent):
            self.connection = parent.connection
            self.cursor = parent.cursor
            sql = '''CREATE TABLE IF NOT EXISTS Ears
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            SkinType VARCHAR(100),
            L_ID INT,
            R_ID INT,
            FOREIGN KEY(L_ID) references Ear(ID),
            FOREIGN KEY(R_ID) references Ear(ID)
            )'''
            self.cursor.execute(sql)
            self.connection.commit()

    class Ear:
        def insert_into_table(self, size, skintype, side, path, legacy):
            sql = '''INSERT INTO Ear (Size, SkinType, Side, Path, Legacy) VALUES ('{}','{}','{}','{}','{}');'''.format(size,
                                                                                                             skintype,
                                                                                                             side,
                                                                                                             path,
                                                                                                             legacy)
            self.cursor.execute(sql)
            self.connection.commit()

        def __init__(self, parent):
            self.connection = parent.connection
            self.cursor = parent.cursor
            sql = '''CREATE TABLE IF NOT EXISTS Ear
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Size VARCHAR(100),
            SkinType VARCHAR(100),
            Side VARCHAR(100),
            Path VARCHAR(300),
            Legacy VARCHAR(100)
            )'''
            self.cursor.execute(sql)
            self.connection.commit()

    class EyeBrows:
        def insert_into_table(self, skintype, L_ID, R_ID):
            sql = '''INSERT INTO EyeBrows (SkinType, L_ID, R_ID) VALUES ('{}',{},{});'''.format(skintype, L_ID, R_ID)
            self.cursor.execute(sql)
            self.connection.commit()

        def __init__(self, parent):
            self.connection = parent.connection
            self.cursor = parent.cursor
            sql = '''CREATE TABLE IF NOT EXISTS EyeBrows
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            SkinType VARCHAR(100),
            L_ID INT,
            R_ID INT,
            FOREIGN KEY(L_ID) references EyeBrow(ID),
            FOREIGN KEY(R_ID) references EyeBrow(ID)
            )'''
            self.cursor.execute(sql)
            self.connection.commit()

    class EyeBrow:
        def insert_into_table(self, size, colour, skintype, side, path, legacy):
            sql = '''INSERT INTO EyeBrow (Size, Colour, SkinType, Side, Path, Legacy) VALUES ('{}','{}','{}','{}','{}','{}');'''.format(
                size, colour, skintype,
                side,
                path, legacy)
            self.cursor.execute(sql)
            self.connection.commit()

        def __init__(self, parent):
            self.connection = parent.connection
            self.cursor = parent.cursor
            sql = '''CREATE TABLE IF NOT EXISTS EyeBrow
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Size VARCHAR(100),
            Colour VARCHAR(100),
            SkinType VARCHAR(100),
            Side VARCHAR(100),
            Path VARCHAR(300),
            Legacy VARCHAR(100)
            )'''
            self.cursor.execute(sql)
            self.connection.commit()

    class Hair:
        def insert_into_table(self, hairtype, colour, skintype, path):
            sql = '''INSERT INTO Hair (HairType, Colour, SkinType, Path) VALUES ('{}','{}','{}','{}');'''.format(
                hairtype, colour, skintype, path)
            self.cursor.execute(sql)
            self.connection.commit()

        def __init__(self, parent):
            self.connection = parent.connection
            self.cursor = parent.cursor
            sql = '''CREATE TABLE IF NOT EXISTS Hair
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            HairType VARCHAR(100),
            Colour VARCHAR(100),
            SkinType VARCHAR(100),
            Path VARCHAR(300)
            )'''
            self.cursor.execute(sql)
            self.connection.commit()

    class AttributeAssignment:  # AttributeAssignment
        # TODO: add foregin key for EyeBrows!
        def insert_into_table(self, faceID, eyesID, eyebrowsID, noseID, mouthID, earsID, hairID):
            sql = '''INSERT INTO AttributeAssignment (FaceID, EyesID, EyeBrowsID, NoseID, MouthID, EarsID, HairID)
            VALUES ({},{},{},{},{},{},{});'''.format(faceID, eyesID, eyebrowsID, noseID, mouthID, earsID, hairID)
            self.cursor.execute(sql)
            self.connection.commit()

        def __init__(self, parent):
            self.connection = parent.connection
            self.cursor = parent.cursor
            sql = '''CREATE TABLE IF NOT EXISTS AttributeAssignment
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            FaceID INTEGER,
            EyesID INTEGER,
            EyeBrowsID INTEGER,
            NoseID INTEGER,
            MouthID INTEGER,
            EarsID INTEGER,
            HairID INTEGER,
            FOREIGN KEY(FaceID) references Face(ID),
            FOREIGN KEY(EyesID) references Eyes(ID),
            FOREIGN KEY(EyeBrowsID) references EyeBrows(ID),
            FOREIGN KEY(NoseID) references Nose(ID),
            FOREIGN KEY(MouthID) references Mouth(ID),
            FOREIGN KEY(EarsID) references Ears(ID),
            FOREIGN KEY(HairID) references Hair(ID)
            )'''
            self.cursor.execute(sql)
            self.connection.commit()

    class Appearance:  # Appearance
        def insert_into_table(self, assignmentID, skintype, filePath):
            sql = '''INSERT INTO Appearance (AssignmentID, SkinType, Date, Path) VALUES ({},'{}',DATETIME('now','localtime'),'{}');'''.format(
                assignmentID, skintype, filePath)
            self.cursor.execute(sql)
            self.connection.commit()

        def __init__(self, parent):
            self.connection = parent.connection
            self.cursor = parent.cursor
            sql = '''CREATE TABLE IF NOT EXISTS Appearance
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            AssignmentID INTEGER,
            SkinType VARCHAR(100),
            Date VARCHAR(100),
            Path varchar(300),
            FOREIGN KEY(AssignmentID) references AttributeAssignment(ID)
            )'''
            self.cursor.execute(sql)
            self.connection.commit()

if __name__ == "__main__":
    db = DbProvider()
    # # first face
    # db.addEyes("small", "blue", "white", "InputFace-01")
    # db.addEars("small", "white", "InputFace-01")
    # db.addEyeBrows("small", "bright", "white", "InputFace-01")
    # db.addNose("small", "white", "InputFace-01")
    # db.addMouth("small", "white", "InputFace-01")
    # db.addHair("long", "bright", "white", "InputFace-01")
    # db.addFace("white", "small", "InputFace-01")
    # # second face
    # db.addEyes("small", "brown", "white", "InputFace-02")
    # db.addEars("small", "white", "InputFace-02")
    # db.addEyeBrows("small", "dark", "white", "InputFace-02")
    # db.addNose("small", "white", "InputFace-02")
    # db.addMouth("small", "white", "InputFace-02")
    # db.addHair("long", "dark", "white", "InputFace-02")
    # db.addFace("white", "small", "InputFace-02")
    # # third face
    # db.addEyes("small", "blue", "white", "InputFace-03")
    # db.addEars("small", "white", "InputFace-03")
    # db.addEyeBrows("small", "bright", "white", "InputFace-03")
    # db.addNose("small", "white", "InputFace-03")
    # db.addMouth("small", "white", "InputFace-03")
    # db.addHair("long", "bright", "white", "InputFace-03")
    # db.addFace("white", "small", "InputFace-03")
    # # 4th face
    # db.addEyes("small", "blue", "white", "InputFace-04")
    # db.addEars("small", "white", "InputFace-04")
    # db.addEyeBrows("small", "bright", "white", "InputFace-04")
    # db.addNose("small", "white", "InputFace-04")
    # db.addMouth("small", "white", "InputFace-04")
    # db.addHair("long", "bright", "white", "InputFace-04")
    # db.addFace("white", "small", "InputFace-04")
    # # 5th face
    # db.addEyes("small", "blue", "white", "InputFace-05")
    # db.addEars("small", "white", "InputFace-05")
    # db.addEyeBrows("small", "bright", "white", "InputFace-05")
    # db.addNose("small", "white", "InputFace-05")
    # db.addMouth("small", "white", "InputFace-05")
    # db.addHair("long", "bright", "white", "InputFace-05")
    # db.addFace("white", "small", "InputFace-05")
    # # 6th face
    # db.addEyes("medium", "brown", "white", "InputFace-06")
    # db.addEars("medium", "white", "InputFace-06")
    # db.addEyeBrows("medium", "dark", "white", "InputFace-06")
    # db.addNose("medium", "white", "InputFace-06")
    # db.addMouth("medium", "white", "InputFace-06")
    # db.addHair("short", "dark", "white", "InputFace-06")
    # db.addFace("white", "medium", "InputFace-06")
    # # 7th face
    # db.addEyes("medium", "brown", "white", "InputFace-07")
    # db.addEars("medium", "white", "InputFace-07")
    # db.addEyeBrows("medium", "dark", "white", "InputFace-07")
    # db.addNose("medium", "white", "InputFace-07")
    # db.addMouth("medium", "white", "InputFace-07")
    # db.addHair("short", "dark", "white", "InputFace-07")
    # db.addFace("white", "medium", "InputFace-07")
    # # 8th face
    # db.addEyes("medium", "blue", "white", "InputFace-08")
    # db.addEars("medium", "white", "InputFace-08")
    # db.addEyeBrows("medium", "bright", "white", "InputFace-08")
    # db.addNose("medium", "white", "InputFace-08")
    # db.addMouth("medium", "white", "InputFace-08")
    # db.addHair("short", "bright", "white", "InputFace-08")
    # db.addFace("white", "medium", "InputFace-08")
    # # 9th face
    # db.addEyes("medium", "blue", "white", "InputFace-09")
    # db.addEars("medium", "white", "InputFace-09")
    # db.addEyeBrows("medium", "bright", "white", "InputFace-09")
    # db.addNose("medium", "white", "InputFace-09")
    # db.addMouth("medium", "white", "InputFace-09")
    # db.addHair("short", "bright", "white", "InputFace-09")
    # db.addFace("white", "medium", "InputFace-09")
    # # 10th face
    # db.addEyes("medium", "blue", "white", "InputFace-10")
    # db.addEars("medium", "white", "InputFace-10")
    # db.addEyeBrows("medium", "dark", "white", "InputFace-10")
    # db.addNose("medium", "white", "InputFace-10")
    # db.addMouth("medium", "white", "InputFace-10")
    # db.addHair("short", "dark", "white", "InputFace-10")
    # db.addFace("white", "medium", "InputFace-10")
    # db.random_features("white")