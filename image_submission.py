import requests
import praw

creds = {"client_id": "X",
         "client_secret": "X",
         "password": "X!",
         "user_agent": "Post an image"
         "username": "5o7bot"}
reddit = praw.Reddit(client_id=creds["client_id"],
                     client_secret=creds["client_secret"],
                     password=creds["password"],
                     user_agent=creds["user_agent"],
                     username=creds["username"])

url = "https://www.themoviedb.org/t/p/original/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg"
response = requests.get(url)
with open("image.jpg", "wb") as f:
    f.write(response.content)

title = 'My favorite picture'
image = 'image.jpg'
reddit.subreddit('5o7bot').submit_image(title, image)
