## App that stores data and checks the input of the user if it's stored if not, adds it .##
import json

data_path = 'data.json'

with open(data_path, 'r') as file:
    data = json.load(file)

user_topic = input("what is the topic?").lower()

for platform in data.keys():
    if user_topic in data[platform]:
        print(user_topic + " is posted on " + platform)
        answer = input(f"Do you wanna remove it? (yes or no)").lower()
        if answer == "yes":
            data[platform].remove(user_topic)
            print(f"{user_topic} is removed from {platform}.")
        else:
            print(f"{user_topic} is not removed from {platform}.")
    else:
        print(user_topic + " is not posted onn " + platform)
        answer = input(f"Do you wanna add it to {platform} ? (yes or no)").lower()
        if answer == "yes":
            data[platform].append(user_topic)
            print(user_topic + "is added to " + platform)
        else :
            print(f"{user_topic} is not added to {platform}")

with open(data_path, 'w' ) as file:
    json.dump(data, file, indent=4)