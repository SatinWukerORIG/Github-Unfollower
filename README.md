# Github-Unfollower
Unfollow everyone you followed on GitHub using Python Selenium Chrome driver

# Principle
1. Login to your GitHub account using your password and username
2. Find your following list
3. Use Selenium to press the unfollow buttons

# Usage
```
usage: python3 unfollow.py [username] [password] [maxpage]

positional arguments:
  username    Your Github username
  password    The password of your Github account for login
  maxpage     Github page number

optional arguments:
  -h, --help  show this help message and exit
 ```
 
 Example:
 `python unfollower SatinWuker passswooord 4`
 
 # Requirements
 This is the libraries that are required: [requirements](requirements.txt)
