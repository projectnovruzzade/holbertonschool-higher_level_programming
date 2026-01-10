#!/usr/bin/python3
""" this is external enviroment"""

import requests
import csv


def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        datas = response.json()
        for data in datas:
            print(data["title"])


def fetch_and_save_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        datas = response.json()
        newData = []
        for data in datas:
            temp = {}
            temp["id"] = data["id"]
            temp["title"] = data["title"]
            temp["body"] = data["body"]
            newData.append(temp)
        print(newData)
        with open("posts.csv", "w", newline="", encoding="utf-8") as file:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(newData)
