# FaceGeneratorApp [[PL]](PrzeczytajMnie.md) 
FaceGeneratorApp is an database project written in Python, JavaScript, and SQL

## Description
Using the **Face Generator Desktop App** we map the faces generated by AI: https://generated.photos/.  
Based on the received map, we separate the input image into images of individual features, we store information about them in the Database.  
Then, using the main application ([**FaceGeneratorApp.py**](FaceGeneratorMainApp/FaceGeneratorApp.py)) we generate random faces from the elements available in the database.  

Database schema used to create the application:
![DatabaseDiagram](FaceGeneratorMainApp/DatabaseBackend/DB_Diagram.png)

### DbProvider
* `random_features` - randomizes features from the database
* `addEyes` - adds a pair of eyes to the database
* `addEars` - add a pair ears to the database
* `addEyeBrows` - adds a pair of eyebrows to the database
* `addNose` - adds a nose to the database
* `addMouth` - adds a mouth to the database
* `addHair` - adds hair to the database
* `addFace` - adds a face template (contour without sub-features) to the database
* `addAttributeAssignment` - creates an assignment of selected face elements and adds to the AttributeAssignment table
* `addAppearance` - adds an appearance to the database

To simplify the creation of entries in the database, it is limited to using the following sample data:
* eye colors [blue, green, black, brown]
* skin types [white, black]
* eyeBrows colours [bright, dark]
* hair colours [bright, dark]
* hair type[long, short]
* sizes [small, medium, large]

## Generator - class used to image generation
* `get_files` - loads and scales selected images
* `insert_feature` - places selected features on the image
* `convert_to_rgba` - adds transparency to image
* `write_face` - saves the generated image
* `create_face` - creates an image with features

### FilesCreator - class used to creating feature images based on FGDA map data
* `cut_feature` - cuts a feature with the given image
* `cut_face` - cuts face (contour) without sub-features
* `convert_to_rgba` - adds transparency
* `create_files` - saves the removed features as .png files in the selected folder

### App - main class of the graphical user interface
* `__init__` - constructor that initializes application subpages
* `exit_callback` - destructor
* `make_window_bigger` - increases the size of the displayed window
* `make_window_smaller` - reduces the size of the displayed window
* `show_frame` - changes the display page
* `resource_path` - returns the path to the file

### Menu - class that defines the appearance of the Menu page
* `__init__` - constructor that initializes page elements
* `setTheme` - sets the color of the page theme and the necessary images
* `createMenu` - sets the menu layout
* `createSpace` - creates a space between interface elements
* `customButton` - creates a personalized button
* `helpButton` - creates a button that displays info about the application


### GeneratorPage - class responsible for the generator interface
* `__init__` - constructor that initializes page elements
* `runGenerator` - starts a new thread with the generator
* `_runGenerator` - performs the generation process
* `file_path` - returns the path to the file
* `loadImage` - loads the given image
* `resize` - changes the size of the displayed image
* `getXY` - get the current window size
* `createHeader` - creates a page header
* `changeImage` - changes the displayed image
* `randomFeatures` - calls the method for randomizing features
* `changeData` - changes the data displayed next to the image
* `changeGenerated` - sets the data of the last generated image
* `createDataTable` - creates tables for information about the generated image
* `createImageFrame` - creates a frame in which the generated image is displayed
* `createBody` - creates page body (space for image and data)
* `setTheme` - sets the color of the page theme and the necessary images

### DatabasePage - class responsible for presenting data from the database
* `__init__` - constructor that initializes page elements
* `setTheme` - sets the color of the page theme and the necessary images
* `createMenu` - creates a page maintenance menu
* `createSpace` - creates a space between interface elements
* `customButton` - creates a personalized button
* `customPandasTable` - creates a personalized table for presenting data
* `enterCallback` - event handling = pressing the 'Enter' button
* `callback` - update data in the table
* `createButton` - creates a button used to update the presented data
* `createEntry` - creates an input field for determining the presented table


## Tools
* Python 3.6.6
* Sqlite3
* Tkinter
* Pillow `pip install Pillow==7.0.0`
* OpenCv `pip install opencv-python==4.2.0.32`
* Pandas `pip install pandas==0.22.0`
* PandasTable `pip install pandastable==0.12.1`
* JavaScript
* Electron 

## How to run FaceGeneratorApp
### First way: 
To use the application you must install [Python 3.6.6](https://www.python.org/downloads/release/python-366/)
and necessary libraries.  
  
Go into FaceGeneratorMainApp directory and run this command - `python FaceGeneratorApp.py`.
This will launch the application in windowed mode.
### Second way:
Go to project directory and run FaceGeneratorApp.exe

## How to start with FaceGeneratorApp
After starting the application, two DB/ and Files/ folders will be created.    
The DB directory contains a database file and Files folder contains a Features subfolder.   
Use FGDA and FilesCreator.py tools to create the appropriate files.   
Put the folder created by FilesCreator in Files/Features/ and go back to FaceGeneratorApp.  
Go to "Database" page and click "InsertData" button. Now you can select the appropriate data.  
In input field "Directory" please type name of the folder created by FilesCreator.  
Finally select "Insert" button and go to Generator page to generate random faces.


## Future improvements
* Code refactoring
* Improved generator operation (optimization of element placement)

## How to run FilesCreator
To use the application you must install [Python 3.6.6](https://www.python.org/downloads/release/python-366/)
and necessary libraries.  
  
Go into FaceGeneratorMainApp directory and run this command - `python FilesCreator.py`.
This will launch the application in console mode.

## Face Generator Desktop App
### What is Face Generator Desktop App (FGDA)
Face Generator Desktop App (FGDA) is written in JavaScript using Electron framework.  
You can read more about Electron [here](https://www.electronjs.org/docs)

FGDA is a simple desktop app that's used to select proper masks/vectors of given face.
Using FGDA we can select:
* Face mask
* Left ear mask
* Right ear mask
* Left eye mask
* Right eye mask
* Left eyebrow mask
* Right eyebrow mask
* Hair mask
* Mouth mask
* Nose mask

Those masks are a 2 dimensional arrays. Each array contains arrays with two values. Those values are **x** and **y** position of a point.
Later those points are used to cut image into proper pieces which are used in generator.

**Sample data**
```
{
  "face":[[5,477],[17,452],[32,432],[44,415],[52,399],[56,385],[60,365],[64,320],[65,292],[70,263],[76,214],[80,190],[84,160],[93,123],[104,97],[115,80],[129,59],[142,41],[165,23],[181,16],[204,7],[217,5],[241,4],[276,3],[299,7],[330,24],[353,42],[373,62],[395,97],[407,123],[424,168],[428,201],[440,254],[448,288],[464,321],[477,343],[479,357],[478,479]],
  "l_eye":[[216,232],[209,223],[201,217],[191,212],[172,212],[158,215],[149,222],[143,230],[143,236],[156,243],[175,243],[191,242],[206,239],[215,235]],
  "r_eye":[[272,230],[278,219],[287,213],[298,210],[315,210],[324,213],[331,219],[337,226],[339,234],[323,241],[303,243],[291,242],[282,239],[274,236]],
  "mouth":[[190,342],[198,341],[205,337],[212,335],[218,331],[224,329],[228,328],[235,329],[241,332],[246,331],[252,329],[255,329],[262,332],[267,336],[271,338],[278,339],[282,339],[286,340],[288,340],[282,346],[274,348],[267,352],[255,357],[245,358],[233,358],[224,357],[212,353],[203,350],[196,348],[192,346]],
  "nose":[[224,303],[215,301],[206,297],[204,292],[204,286],[207,277],[210,271],[214,266],[217,261],[221,256],[222,252],[224,245],[225,239],[226,233],[226,228],[227,224],[233,221],[242,221],[247,222],[250,226],[251,233],[253,241],[255,250],[258,261],[262,269],[265,277],[270,285],[272,290],[270,298],[267,302],[260,305],[252,306],[244,303],[237,302],[231,304]],
  "l_ear":[[122,303],[119,290],[113,275],[108,265],[107,255],[105,267],[102,290],[102,299],[108,304],[115,306],[119,306]],
  "r_ear":[[367,309],[374,309],[382,310],[384,301],[384,290],[380,279],[374,266],[370,287],[368,298]],
  "hair":[[229,83],[255,84],[277,90],[304,96],[320,114],[336,153],[350,193],[367,237],[373,260],[382,281],[384,291],[384,301],[382,312],[375,308],[368,308],[359,334],[351,357],[336,381],[345,404],[344,420],[338,446],[328,466],[313,479],[479,477],[478,359],[476,340],[464,324],[448,289],[440,256],[427,204],[422,170],[407,124],[395,101],[371,62],[352,44],[332,25],[298,10],[276,5],[242,4],[215,7],[206,7],[179,15],[163,22],[142,41],[133,59],[115,80],[100,96],[94,122],[86,161],[81,188],[76,218],[71,261],[65,296],[62,320],[58,368],[57,385],[53,396],[44,418],[36,432],[18,453],[5,478],[161,477],[161,449],[159,420],[156,400],[151,379],[140,363],[128,344],[123,326],[121,308],[112,304],[105,299],[101,296],[101,286],[102,280],[104,262],[107,255],[107,241],[109,218],[112,196],[116,175],[120,157],[125,136],[136,122],[147,109],[164,95],[181,89],[202,84],[215,82]],
  "l_eyebrow":[[130, 205],[139, 202],[149, 198],[162, 201],[173, 201],[185, 200],[197, 200],[205, 200],[212, 199],[216, 196],[211, 192],[200, 187],[183, 187],[169, 186],[158, 186],[147, 189],[136, 195],[132, 199]],
  "r_eyebrow":[[268, 200],[276, 191],[291, 188],[306, 186],[324, 186],[336, 191],[345, 199],[331, 198],[317, 196],[297, 196],[282, 198]]
}
```
**Application GUI**
![alt text](https://github.com/ReQezeR/FaceGeneratorApp/blob/master/FaceGeneratorDesktop/sampleFGDA.png "FGDA GUI")

### How to run Face Generator Desktop App (FGDA)
You need to install [Node.js](https://nodejs.org/en/) to be able to use [npm](https://www.npmjs.com/) packages.

Go into FaceGeneratorDesktop directory and run this command - 
`npm install`.
This command will install all packages.
Then if you want to run app use - 
`npm start`.
It will start the app in debug mode (with console open).

## Credits
* **Michał Popiel** - *GUI, Generator* - [ReQezeR](https://github.com/ReQezeR)
* **Nikodem Janaszak** - *Database* [NikodemJanaszak](https://github.com/NikodemJanaszak)
* **Jakub Kusiowski** - *Data creation application (FGDA)* [JKusio](https://github.com/JKusio)
* **Norbert Młynarski** - *Concurrency* [bibiosm98](https://github.com/bibiosm98)


## License: [MIT](https://choosealicense.com/licenses/mit/)

## Summary
The project was conducted during the Database Lab course, Poznan University of Technology.  
Supervisor: [**DR INŻ. KRZYSZTOF ZWIERZYŃSKI**](https://sin.put.poznan.pl/people/details/krzysztof.zwierzynski)
