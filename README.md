# SNIPPET CONSOLE


### Snippet console is a text saving and retrieval django application developed in django 3.2.9 and python 3.9

   
#### How to run snippet_console ####

1. Clone snippet_console project from below url to the Project directory
   ```
    $ cd ~/Projects
    $ git clone https://github.com/lijoev/snippet_console.git
   ```

2. project dependencies are managed by requirements.txt file. See the files for dependency list
 
   
3. Environment variables are managed using `python decouple module` and `.env file`
   ```
    Enviroment variables explained below.
    1. SECRET_KEY: Secret key for django application
    2. DATABASES_NAME: Database name for snippet application
    3. DEVELOPMENT: Boolean value to specify the app is in developement or not
    4. DEBUG: Boolean value to specify debug
    5. SNIPPETCONSOLE_SETTINGS_MODULE: Doted path for the settings file to use. Use development.py for developement and production.py for production environment
   
   ```
4. Rename the ```env_template``` file to ```.env``` and keep it in root directory


5. Set up the python virtual environment and project dependencies by following below steps
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

