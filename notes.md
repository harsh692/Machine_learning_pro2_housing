## June 18/19/25

1. create setup.py file with setup functions  
    * run  this command to install all the requirements.
        ```
        pyton setup.py install 
        ```

2. Project structure :
    1. housing folder
        1. __init__.py
        2. exception package
        3. logger package
        4. pipeline package
        5. component
        6. config
        7. entity

    2. creating logger
        : all the logs are to be recorded in a special logging directory.
        We are going to create logging using the logging module available in the 
        python.
 
    3. creating exception   
        : Creating our own custom exception class inheriting from Exception class
        from python , which will return exception msg with some extra important message.

    4. Project overview :
        creating a proper structure of how ml creation will proceed.
        * using serialization and deserialization for the purpose of saving the model,
          in the form of an object and using it again. We make use of pickle module 
          for the purpose of serialization.   

    5. creating component folder :   
        #### Contents :    (all these are python files)
        1. data ingestion  
        2. data validation  
        3. data transformation  
        4. model trainer  
        5. model evaluation  
        6. model pusher  
        7. __init__ file  

    6. creating pipeling folder :   
        #### Contents : 
        1. __init__ file  
        2. pipeline.py    

    7. creating entity folder   (Config and entity are very important)
        : entity can be defined as any interpretable object , enitity is associated with
          database.

        example : STUDENT_DATABASE MANGAGEMENT SYSTEM -->
                ENTITES : 
                    * classroom
                    * exam   
                    * student etc.   

        #### Description :   
        * In the entity we define an artefact for each and every component of the 
          machine learning pipeling.
          ex :  1. data ingestion artefact
                2. data validation artefact  
                3. data transformation artefact  
                4. model trainer artefact  
                5. model evaluation artefact  
                6. model pusher artefact   

                an artefact can be understood as a result we will get from
                completing a scientific process , here a component of pipeline .
        * In the entity , for the each component of pipeline , some data is to be
          input, this is called as data configuration.
          ex :  1. data ingestion config  
                2. data validation config  
                etc.

        ### Creation :   
        1. create entity_config.py  
        2. create named tuples for each of the configurations in entity  
                ex. <name> = namedtuple("<name>",[-------names of tuple------])

        3. in step 2 we have defined the structures of all the entities.
        4. For the configuration we have to provide the defined information , but from where we provied is upto us.  
        5. All the information here , we are going to provide by a yaml file.  
            yaml file, json file etc. are the files to store data in a particular fasion.  
            we can also use json file, csv file, data base connector directly etc.  
            here we are going to use yaml file.
        6. 