SQLAlchemy Climate Analysis

Welcome to the SQLAlchemy Climate Analysis project! This project aims to provide a climate analysis and exploration of the Honolulu, Hawaii area. 

The analysis is performed using Python, SQLAlchemy ORM queries, Pandas, and Matplotlib. The project includes an interactive Flask API for accessing the climate data.

Project Structure
The project consists of the following main components:

climate_analysis.ipynb: Jupyter Notebook containing the climate analysis and exploration using SQLAlchemy and Pandas.

app.py: Flask application file that creates the routes for the API endpoints and performs the database queries.

Resources: Folder containing the data files used for the analysis (hawaii.sqlite).

Functionality
The project includes the following functionality:

Precipitation Analysis: Retrieves the last 12 months of precipitation data and plots the results.

Station Analysis: Calculates the total number of stations, identifies the most active stations, and retrieves temperature observation data for the most active station.

Flask API: Provides the following API endpoints:

/api/v1.0/precipitation: Retrieves the last 12 months of precipitation data as a JSON dictionary.

/api/v1.0/stations: Returns a JSON list of stations.

/api/v1.0/tobs: Retrieves temperature observations for the most active station in the previous year as a JSON list.

/api/v1.0/<start>: Calculates the minimum, average, and maximum temperatures for a specified start date and returns the results as JSON.

/api/v1.0/<start>/<end>: Calculates the minimum, average, and maximum temperatures for a specified start and end date range and returns the results as JSON.

Setup and Usage
To run the project, please follow these steps:

Clone the repository to your local machine.

Ensure you have the required dependencies installed, such as Flask, SQLAlchemy, Pandas, and Matplotlib.

Open and run the climate_analysis.ipynb Jupyter Notebook to perform the initial climate analysis and exploration.

Execute the app.py Flask application to start the Flask API and access the climate data through the provided endpoints.

Conclusion
The SQLAlchemy Climate Analysis project provides valuable insights into the climate data of Honolulu, Hawaii. The analysis and exploration are performed using Python, SQLAlchemy, Pandas, and Matplotlib. The Flask API allows easy access to the climate data through various endpoints.

Please feel free to reach out if you have any questions or need further assistance.
