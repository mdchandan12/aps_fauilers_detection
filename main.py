import pymongo
import pandas as pd
import json

#Provide the mongodb localhost url to connect python to mongodb
client = pymongo.MongoClient("mongodb://localhost:27017")

Data_File_Path = "aps_failure_training_set1.csv"
DataBase_Name = "aps"
Collection_Name = "sensor"

if __name__=="__main__":
    df = pd.read_csv(Data_File_Path)
    print(f"Rows and Columns: {df.shape}")
    
#Convert dataframe to json so that we can dump these record in mongodb
df.reset_index(drop = True, inplace = True)  

json_record = list(json.loads(df.T.to_json()).values())
print(json_record[0])  

#Insert converted json record to mongodb
client[DataBase_Name][Collection_Name].insert_many(json_record)