import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import praw


def check_if_link_is_already_in_database(posturl, chosen_subreddit, chosen_display_type):
    reference = db.reference("/")
    ids = reference.child(chosen_subreddit).get()
    if ids == None:
        return False
    for id in ids:
        image_link = reference.child(chosen_subreddit).child(id).get()
        if posturl == image_link.get('title'):
            return True
    return False

def get_images_from_subreddit(subreddit, limitation, chosen_display_type):
    reddit = praw.Reddit(client_id='GIVEN CLIENT ID', \
                     client_secret='YOUR GIVEN USER AGENT SECRET CODE', \
                     user_agent='YOUR USER AGENT USERNAME THAT YOU CREATED', \
                     username='YOUR REDDIT USERNAME', \
                     password='YOUR REDDIT ACCOUNT PASSWORD')
    subreddit_access = reddit.subreddit(subreddit)
    if chosen_display_type == '1':
        posts = subreddit_access.controversial(limit=limitation)
        return posts
    elif chosen_display_type == '2':
        posts = subreddit_access.new(limit=limitation)
        return posts
    elif chosen_display_type == '3':
        posts = subreddit_access.top(limit=limitation)
        return posts

def login_to_firebase():
    cred = credentials.Certificate('firebase-adminsdk.json') #THIS JSON FILE CAN BE GENERATED FROM YOUR FIREBASE DATABASE
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://<your firebase database project name>.firebaseio.com/'
    })

def push_links_to_database(chosen_subreddit='lol', limit=0, chosen_display_type='0'):
    if chosen_subreddit=='lol':
        chosen_subreddit = input("subreddit: ")
    if limit==0:
        limit = input("number of images (this can be less than requested as some may have existed beforehand): ")
    if chosen_display_type=='0':
        chosen_display_type = input(" '1' for Controversial Posts\n '2' for New Posts\n '3' for Top Posts\nChoose a type: ")
    reference = db.reference(chosen_subreddit)
    posts = get_images_from_subreddit(chosen_subreddit, int(limit, 10), chosen_display_type)
    count = 0
    counter2 = 0
    for post in posts:
        theresalink = False
        counter2 = counter2 + 1
        if check_if_link_is_already_in_database(post.title, chosen_subreddit, chosen_display_type) == False:
            if post.url.find('https://imgur') > -1:
                url = post.url.replace('https://imgur', 'https://i.imgur')
                url = url + '.jpg'
            elif post.url.find('http://imgur.com/') > -1:
                url = post.url.replace('http://imgur', 'http://i.imgur')
                url = url + '.jpg'
            else:
                url = post.url

            if url.find('jpg') > -1 or url.find('png') > -1 or url.find('jpeg') > -1 or url.find('PNG') > -1 or url.find('JPG') > -1 or url.find('JPEG') > -1:
                if url.find('imgur') > -1 or url.find('redd') > -1:
                    if url.find('jpg') > -1:
                        firstpart, jpg, _ = url.partition("jpg")
                        url = firstpart + jpg
                    if url.find('png') > -1:
                        firstpart, jpg, _ = url.partition("png")
                        url = firstpart + jpg
                    if url.find('jpeg') > -1:
                        firstpart, jpg, _ = url.partition("jpeg")
                        url = firstpart + jpg
                    count = count + 1
                    if url.find("/a/") <= -1 and url.find("/gallery/") <= -1:
                        theresalink = True
                        print("pulled images: " + str(counter2) + " valid images: " + str(count))
                        print(url)

            if theresalink:
                reference.push({
                                'image_source': url,
                                'title' : post.title,
                                'selftext': post.selftext
                            })
            else:
                if chosen_subreddit != 'tinder':
                    reference.push({
                                    'image_source': '',
                                    'title' : post.title,
                                    'selftext': post.selftext
                                })
