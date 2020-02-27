# FaceGeneratorApp
## Overview
FaceGeneratorApp is an database project written in python and sql
## Description
Korzystając z wygenerowanych przez AI twarzy: https://generated.photos/ tworzymy aplikacje, która z dostępnych elementów generuje zmodyfikowane twarze.    
Schemat bazy danych wykorzystany przy tworzeniu aplikacji:
![DatabaseDiagram](DatabaseBackend/DB_Diagram.png)

## Database Methods
* addEyes – dodaje parę oczu do bazy danych
* addEars – dodaje parę uszu do bazy danych
* addEyeBrows – dodaje parę brwi do bazy danych
* addNose – dodaje nos do bazy danych
* addMouth – dodaje usta do bazy danych
* addHair – dodaje włosy do bazy danych
* addFace – dodaje szablon (tło) twarzy do bazy danych
* addAttributeAssignment – tworzy przypisanie wybranych elementów twarzy i dodaje do tabeli AttributeAssignment
* addAppearance – na podstawie AttributeAssignment tworzony jest wpis do tabeli zawierający elementy wygenerowanej twarzy, datę generowania, oraz ścieżkę. 

W celu uproszczenia tworzenia wpisów w bazie danych ograniczono się do skorzystania z następujących przykładowych danych:
* eye colors [blue, green, black, brown]
* skin types [white, black]
* eyeBrows colours [bright, dark]
* hair colours [bright, dark]
* hair type[long, short]
* sizes [small, medium, large]

## Tools
* Python 3.6
* Sqlite / Django

## How to run
* Windows
## Future improvements
* ~~Stworzenie kompletnego schematu bazy danych~~
* ~~Implementacja w SQL(wyzwalacze, procedury składowane)~~
* ~~Stworzenie wstępnego algorytmu generowania twarzy~~
* ~~Implementacja testowego generatora~~

## Attributions 
TODO
## Credits
* **Michał Popiel** - *GUI* - [ReQezeR](https://github.com/ReQezeR)
* **Norbert Młynarski** - *Generator-współbieżność* [bibiosm98](https://github.com/bibiosm98)
* **Nikodem Janaszak** - *Database* [NikodemJanaszak](https://github.com/NikodemJanaszak)
* **Jakub Kusiowski** - *Generator* [JKusio](https://github.com/JKusio)


## License
[MIT](https://choosealicense.com/licenses/mit/)

The project was conducted during the Database Lab course, Poznan University of Technology.
Supervisor: Krzysztof Zwierzyński

