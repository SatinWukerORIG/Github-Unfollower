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

In addition, you also need to install the [Chromedriver](https://chromedriver.chromium.org/downloads) that is compatible to your browser. Then, you need to put it with [unfollow.py](unfollow.py), under the same path.
<br>
If you are using Linux or MacOS, you can download Chromedriver-linux64 or Chromedriver-mac64, and change the path in [unfollow.py](unfollow.py), line 5.
