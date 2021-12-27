# SNIPPET CONSOLE


### Snippet console is a text saving and retrieval django application developed in django 3.2.9 and python 3.9

   
#### How to run snippet_console ####

1. Clone snippet_console project from below url to the Project directory
   ```
    $ cd ~/Projects
    $ git clone <github url>
   ```

2. project dependencies are managed by requirements.txt file. See the files for dependency list
 
   
3. Environment variables are managed using `python decouple module` and `.env file`
   ```
    Enviroment variables explained below   
   ```
4. Set up the python virtual environment and project dependencies by following below steps
   1. Navigate to the Project directory using below command
       ```$ cd ~/Projects/snippet_console ```
   2. create the virtual environment using below command
       ```$ python3 -m venv venv```
   3. Activate the virtual environment using below command
       ```$ source venv/bin/activate```
   4. install the project dependencies using below command
       ```$ pip install -r reqirements.txt```
   

5. How to run migrate command
    ```
        $ cd ~/Projects/snippet_console
        $ python manage.py migrate
    ```
6. How to run the project
    ```
    python manage.py runserver
    ```

