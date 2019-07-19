import firebaseshit
from therealdoodleishere import *
import time

login_to_firebase()

limit = input("limit: ")
type = input("1 for controversial - 2 for new - 3 for top: ")
subreddit = input("subreddit: ")
push_links_to_database(subreddit, limit, type)
