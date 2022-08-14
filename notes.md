## June 11

### Deployment : heroku cloud (github rep)   
1. email id  
2. Heroku Api key  
3. App_name  
   linux virtual machine  (500mb free)


### Docker  
1. Portability of code (basically once in docker , you can run the code in any system, we can directly us the software without installing lot of things.)
     
     Example : flask app ---->>>> dockerized and its image is shared and saved in dockerhub.
2. Container (Container is a type of virtual machine)
    Container is a virtualisation of hardware where you can install your requ. and directly run your application.   
    Container is lightweight as it has min req. to run your software.
3. Docker Image 
    * OS : base layer  
    * Instructions to use docker image : create a docker file containing,   
        Example :  
        1. which os  
        2. < set folder >  
        3. copy code  
        4. create venv  
        5. activate venv  
        6. Install req.txt  
        7. cmd python app.py  

    * we need this dockor file/image and docker should be installed.  
    * Docker provides runtime environment  

## June 12  

#### Agenda  
1. Create a flask app(hello world)
2. Write a docker file for flask application  
3. Create github action for CI/CD  
4. Heroku app for flask deployment  
5. Create structure for ml project  
6. Machine learning pipeline  

#### Steps   
1. conda create -p venv python==3.7 -y
2. CI/CD pipeling setup :  
    * heroku email id  
    * heroku api key  
    * heroku app name
3. Build docker image  
    * docker build -t <image_name>:<tagname> <filelocation>
    * to list docker image : docker images  
    * to run docker image : docker run -p 5000:5000 -e port=5000 6db80422c240  
    * to check container running : docker ps  
    * to stop docker container running : docker stop <container_id, here 6db8>
4. Trigger and yaml file
    * set a trigger in yaml file : here whenever there is any push in github repo deployment will be triggered.  
    * Basically we are using github actions to implement a ci/cd pipeline.
    * whenever we change anything in our code in project, it will automatically reflect in out deployed app, with the help of ci/cd in github.
    * push all these changes to github and check actions in github, it will contain the added github work file.
    * if giving error , go to settings and click on secret -->> actions -->> new repositery secrets, create secrets for private info required in github work file such as api key , app name and email. not re load in github actions, it will start working.
    * check on heroku app logs.
    


