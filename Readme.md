# Sam Media report project

## Project Overview
Report of the current situation in the country. 
EDA and pdf report are located in `research/Analysis of subscriptions.ipynb`

### Setting Up the Application

#### 
1. Clone the repository
2. Activate the virtual environment
3. Install requirements.txt
4. To populate model with data from a CSV file:
`python manage.py import_csv`
5. To run the app: `python manage.py runserver`
6. Before running the server for the first time, apply the migrations:
 `python manage.py migrate analytics`
