# Covid-19-data-analysis

# Overview
The web app displays the CARD data of all the states of India using graphs and tables, it also shows the sentiments of the state. The sentiment is calculated by doing a sentiment analysis on the tweets made from the respective states and calculating an average value. The state wise trend is also shown after clciking on a particular state in the state table. A seperate page enables the user to find the patients by using filters 

# Setup
1. Setting up the database:

    i. Go to the setting.py in the backend->home->setting.py.
    
    ii. Look for database and configure the database that you will be using, the database used is a SQL database.
    
    iii. Run the server locally bu the command manage.py runserver.
    
    iv. Now to populate the database, send a empty post request to "localhost/databaseUpdate". This will automatically fetch the data from csv files and enter in the database.
    
2. Linking backend with frontend:

    i. Go to commonFunctions.js in frontend->src->utils->commonFunctions.js.
    
    ii. Make sure the localDatabaseUrl is set to "http://localhost:8000/".
    
3. Host the backend and the frontend locally and you are good to go.
