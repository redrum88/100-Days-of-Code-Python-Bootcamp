# SEPERATOR = ","
#
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
#

# Import CSV package
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     print(data)
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
import math
import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))
#
# data_dict = data.to_dict()
# print(data_dict)
#
# data_list = data["temp"].to_list()
# print(data_list)
#
# print(data["temp"].max())


# print(data[data.day == "Monday"])
#
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]

# (0°C × 9/5) + 32
# faren = (monday.temp * 1.8) + 32
# print(faren)


# Create a dataframe from scratch
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
all_gray = []
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

by_color = data['Primary Fur Color'].value_counts()
print(by_color)

#by_color.to_csv("squirrels_by_color_count.csv")


gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])


print(gray_squirrels)
print(black_squirrels)
print(red_squirrels)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, red_squirrels , black_squirrels]
}

df = pandas.DataFrame(data_dict)

df.to_csv("output.csv")