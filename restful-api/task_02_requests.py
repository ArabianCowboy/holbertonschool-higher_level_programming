#!/usr/bin/python3
"""
Task 02: Consuming and processing data from an API using Python.
Fetch posts from JSONPlaceholder, print titles, and save selected fields to CSV.
"""

import csv
import requests

URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Fetch all posts and print the response status code and each post title."""
    response = requests.get(URL, timeout=10)
    print(f"Status Code: {response.status_code}")

    if response.status_code != 200:
        return

    posts = response.json()
    for post in posts:
        print(post.get("title", ""))


def fetch_and_save_posts():
    """
    Fetch all posts and save them to posts.csv with columns: id, title, body.
    """
    response = requests.get(URL, timeout=10)

    if response.status_code != 200:
        return

    posts = response.json()

    data = [
        {
            "id": post.get("id"),
            "title": post.get("title", ""),
            "body": post.get("body", ""),
        }
        for post in posts
    ]

    with open("posts.csv", "w", newline="", encoding="utf-8") as f:
        fieldnames = ["id", "title", "body"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
