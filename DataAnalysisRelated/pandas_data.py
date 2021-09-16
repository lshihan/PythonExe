### weather_data and new_data
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

# import pandas as pd

# data = pd.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# print(data["temp"].mean())
# print(data["temp"].max())

# # Get data in column(Both code doing same thing)
# print(data["condition"])
# print(data.condition)

# Get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()]
# monday = data[data.day == "Monday"] 
# monday = data[data["day"] == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# Create dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "score" : [76, 56, 65]
# }

# data = pd.DataFrame(data_dict)
# data.to_csv("new_data.csv")


### 2018_Central_Park data
import pandas as pd


data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv") #Convert above arranged data to new csv file.