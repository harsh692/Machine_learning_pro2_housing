## June 18  

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

