import urllib.request
import zipfile
import pandas as pd
from sqlalchemy import create_engine 

download = urllib.request.urlretrieve("https://gtfs.rhoenenergie-bus.de/GTFS.zip", "download.zip")

with zipfile.ZipFile ('download.zip') as myzip:
    myzip.extractall("GTFS_Folder")
    #with myzip.open('stops.txt') as myfile:
        # print(myfile.read())
#data = pd.read_csv (myfile)
#data = pd.read_csv("GTFS_Folder/stops.txt")
data = pd.read_csv("GTFS_Folder/stops.txt", 
    encoding='utf8',
    usecols=['stop_id', 'stop_name', 'stop_lat', 'stop_lon', 'zone_id'],
    dtype={
       'stop_id': int,
       'stop_name': str, 
       'stop_lat': float, 
       'stop_lon': float, 
       'zone_id': int 
    }
)
#columns = ['stop_id', 'stop_name', 'stop_lat', 'stop_lon', 'zone_id']
#df1 = pd.DataFrame(data, columns=columns)
df1 = pd.DataFrame(data)
#print(df1.to_string())
#print(df1.info())

#df2 = df1[df1["zone_id"] == 2001]
#print(df2.to_string)
df2=df1.loc[
    (df1['stop_lat']>=-90)&
    (df1['stop_lat']<=90)&
    (df1['stop_lon']>=-90)&
    (df1['stop_lon']<=90)&
    (df1['zone_id']==2001)
]
#print(df2.info())




# load data to database
engine = create_engine("sqlite:///gtfs.sqlite")

    # Write data into the table in sqllite database, remove index column
df2.to_sql('stops', engine, if_exists='replace', index = False)
#df2.to_sql = ('stops', engine) 

##df2.to_sql('stops', 'sqlite:///gtfs.sqlite', if_exists='replace', index=False)
