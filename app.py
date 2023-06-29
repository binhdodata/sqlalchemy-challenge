from flask import Flask, jsonify

# Create an instance of Flask
app = Flask(__name__)

# Define the home route
@app.route("/")
def home():
    """List all available routes"""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;<br/>"
    )

# Define the precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the JSON representation of precipitation data for the last 12 months"""
    # Perform the query to retrieve the last 12 months of precipitation data
    # Code to perform the query and convert results to a dictionary
    # Replace this code with the query and conversion logic from your previous code

    # Example code to demonstrate the output format
    precipitation_data = {"date1": 1.23, "date2": 2.45, "date3": 0.78}
    
    return jsonify(precipitation_data)

# Define the stations route
@app.route("/api/v1.0/stations")
def stations():
    """Return a JSON list of stations from the dataset"""
    # Perform the query to retrieve the list of stations
    # Code to perform the query and retrieve stations
    # Replace this code with the query logic from your previous code

    # Example code to demonstrate the output format
    station_list = ["Station1", "Station2", "Station3"]

    return jsonify(station_list)

# Define the tobs route
@app.route("/api/v1.0/tobs")
def tobs():
    """Return a JSON list of temperature observations for the most active station in the previous year"""
    # Perform the query to retrieve the temperature observations for the most active station in the previous year
    # Code to perform the query and retrieve temperature observations
    # Replace this code with the query logic from your previous code

    # Example code to demonstrate the output format
    tobs_data = [{"date": "2017-01-01", "temperature": 72},
                 {"date": "2017-01-02", "temperature": 75},
                 {"date": "2017-01-03", "temperature": 70}]
    
    return jsonify(tobs_data)

# Define the start route
@app.route("/api/v1.0/<start>")
def temperature_start(start):
    """Return a JSON list of the minimum, average, and maximum temperatures for a specified start date"""
    # Perform the query to calculate the minimum, average, and maximum temperatures for the specified start date
    # Code to perform the query and calculate temperatures
    # Replace this code with the query logic from your previous code

    # Example code to demonstrate the output format
    temperature_data = {"start_date": start,
                        "TMIN": 65,
                        "TAVG": 73,
                        "TMAX": 80}
    
    return jsonify(temperature_data)

# Define the start/end route
@app.route("/api/v1.0/<start>/<end>")
def temperature_start_end(start, end):
    """Return a JSON list of the minimum, average, and maximum temperatures for a specified start-end range"""
    # Perform the query to calculatethe minimum, average, and maximum temperatures for the specified start and end dates
    # Code to perform the query and calculate temperatures
    # Replace this code with the query logic from your previous code

    # Example code to demonstrate the output format
    temperature_data = {"start_date": start,
                        "end_date": end,
                        "TMIN": 65,
                        "TAVG": 73,
                        "TMAX": 80}
    
    return jsonify(temperature_data)

# Run the application
if __name__ == "__main__":
    app.run(debug=True)