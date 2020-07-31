# Covid-19-data-analysis

1. Setting up the database:
    i. Go to the setting.py in the backend->home->setting.py.
    ii. Look for database and configure the database that you will be using, the database used is a SQL database.
    iii. Run the server locally bu the command manage.py runserver.
    iv. Now to populate the database, send a empty post request to "localhost/databaseUpdate". This will automatically fetch the data from csv files and enter in the database.
    
2. Linking backend with frontend:
    i. Go to commonFunctions.js in frontend->src->utils->commonFunctions.js.
    ii. Make sure the localDatabaseUrl is set to "http://localhost:8000/".
    
3. Host the backend and the frontend locally and you are good to go.
