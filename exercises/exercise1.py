import pandas as pd
from sqlalchemy import create_engine

# extract data from source
source = 'https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv'
data = pd.read_csv (source, sep=';')

# column_1;column_2;column_3;column_4;column_5;column_6;column_7;column_8;column_9;column_10;column_11;column_12;geo_punkt
# 8703;Barberton Airport;Barberton;South Africa;0;FABR;-25.716869;30.97518;686;2.0;U;Africa/Johannesburg;-25.716869, 30.97518
# 330;Jena-Schöngleina Airport;Jena;Deutschland;0;EDBJ;50.915279388427734;11.714444160461426;380;1.0;E;Europe/Berlin;50.9152793884, 11.7144441605

# fields:
#  [{"name": "column_1",
#  "description": "Eindeutige OpenFlights-Kennung f\u00fcr diesen Flughafen.", 
# "type": "int"}, 
# {"name": "column_2", 
#  "label": "Name des Flughafens", 
# "type": "text"}, 
# {"name": "column_3", 
# "label": "Ort", 
# "type": "text"}, 
# {"name": "column_4", 
# "label": "Land", 
# "type": "text"}, 
# {"name": "column_5", 
# "description": "IATA-Flughafencode mit 3 Buchstaben. Null wenn nicht zugewiesen bzw. unbekannt.", 
# "label": "IATA", 
# "type": "text"}, 
# {"name": "column_6", 
# "description": "ICAO-Code mit 4 Buchstaben zur eindeutigen Identifizierung des Flugpl\u00e4tzes. Null wenn nicht zugewiesen bzw. unbekannt.", 
# "label": "ICAO", 
# "type": "text"}, 
# {"name": "column_7", 
# "description": "Breitengrad als Dezimalgrad; negativ ist S\u00fcden, positiv ist Norden.", 
# "label": "Latitude", 
# "type": "text"}, 
# {"name": "column_8", 
# "description": "L\u00e4ngengrad als Dezimalgrad; negativ ist West, positiv ist Ost.", 
# "label": "Longitude", 
# "type": "text"}, 
# {"name": "column_9", 
# "description": "H\u00f6he in Meter", 
# "label": "Altitude", 
# "type": "int"}, 
# {"name": "column_10", 
# "description": "Zeitverschiebung von UTC", 
# "label": "Zeitzone", 
# "type": "double"}, 
# {"name": "column_11", 
# "description": "Daylight Saving Time (Sommerzeit)\nE (Europe), A (US/Canada), S (South America), O (Australia), Z (New Zealand), N (None), U (Unknown)", 
# "label": "DST", 
# "type": "text"}, 
# {"name": "column_12", 
# "label": "Zeitzonen-Datenbank", 
# "type": "text"},
#  {"name": "geo_punkt", 
# "label": "geo_punkt", 
# "type": "geo_point_2d"}]

# load data to database
engine = create_engine("sqlite:///airports.sqlite")

# create a table in the database
# class airport:
#    __tablename__ = 'airport'

# Write data into the table in sqllite database 
data.to_sql('airports', engine) 