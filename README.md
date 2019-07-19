# FaceLife
#### [here's a sample for the chatbot in it's working state (leave a like <3)](https://www.facebook.com/FaceLife-437256150456258/?ref=settings)

  When i'm using Free Facebook i don't get to see pictures nor memes outside of only chat messages, so i made this quick chatbot using [Dialogflow](https://dialogflow.com) and [Facebook For Developers](https://developers.facebook.com) and throughout my work i found out you can send an image using its link from [Dialogflow](https://dialogflow.com) to Facebook using the `agent.add()` line in the Fulfillment tab, it will count it as if you've uploaded it and so! you can see it on Free Facebook! here's how you can do it and for free.
  
  It's a three part process:
  ## 1) Setting up Dialogflow:
  
  ### Step 1:
  head on [Dialogflow](https://dialogflow.com) and create a project.
  
  ### Step 2:
  go to the Integrations tab and setup the Facebook Messenger integration ([here's a good tutorial](https://www.youtube.com/watch?v=-2hE3YHsuBQ)).
  
  ### Step 3:
  now you can create intents in the Intent section, name it with your subreddit's name (without the r/ so for example tinder **ALL LOWER CASE**), we're going to use these intents to detect what the user is asking us to deliver, and so create a new intent and add a Training Phrase in the Training Phrase section containing a subreddit (for ex. r/tinder) (if the user types this then the intent gets triggered), scrolling down to the Fulfillment section click it & check `Enable Web hook call for this intent`, save and exit.
  
  ### Step 4:
  in the Intents list there's a default Fallback Intent, this intent is run everytime our user has typed anything other than the available subreddits, open it & head down to the answer section and select the "Facebook Messenger" tab, remove whatever is in there & add a new Quick reply, this is a menu that will appear in the chat letting the user choose what to quickly type instead of typing it themselves (works on Free Facebook).
  
  ### Step 5:
  in your project settings you must get `Project ID` as we need it for the next step.
  
  ### Step 6:
  now head to the Fulfilment tab & enable `Inline Editor` paste the code from `dailogflow_fulfillment_code/index.js` above in the files section into there replacing everything.
  
  put your Project ID here replacing the brackets and all what's inside:
  ```
  databaseURL: 'ws://<your firebase database project>.firebaseio.com/',
  ```
  
  go down below where you find (and do as instructed): **ALL LOWER CASE**
  ```
  function niceguys(agent){ return save("niceguys"); }                 // what's between the quotes is the subreddit
  function minecraft(agent){ return save("minecraft"); }               // name, note that i
  //add a function for every subreddit like the examples above here ^  // always use lowercasing to keep consistency.
  ```
  >NOTE: these nominations are case sensitive so keep everything in lowercase to keep consistency
  >scroll further until you see (and do as instructed):
  ```
  intentMap.set('creepypms', creepypms); // what's between quotes in the intent title, and on its right is the function name ^
  intentMap.set('niceguys', niceguys);
  intentMap.set('minecraft', minecraft);
  //add a intentmap for every subreddit like the examples above here ^
  ```
  >NOTE: these nominations are case sensitive so keep everything in lowercase to keep consistency
  
  
  
  then click on the `package.json` section and paste `dailogflow_fulfillment_code/package.json` in there.
  click deplay and wait until a green dialog appears in the corner.
  
   ## 2) Setting up the Realtime Firebase Database:
  
  This is the easier step as all you need to do is head on [your firebase project list](https://console.firebase.google.com/u/0/) & going on the project with your Project ID on it.
  
  Head to the `Database` tab & create a Realtime Database (not the Cloud Firestore, you must click on wherever it says Cloud Firestore & actually switch onto the Realtime Database if it isn't selected already).
  
  That's it!
  
  ## 3) Actually filling up the database with posts:
  
  Firebase is a good fella, allows your database to hold up to 5GB of storage which could hold about 123 million links to images (if you decided not to pull the titles and post text from subreddits like i did in the code), and that's enough memes for a lifetime.
  
  I've made a quick python script that goes on reddit using the `PRAW` library made specifically for Reddit (lizom), but:
  
  ### Step 1:
  To get access you must register a Reddit application from [here](https://www.reddit.com/prefs/apps/), you will need most of the information given so keep that page open.
  
  ### Step 2:
  Download the Python files inside the `filling_the_database_with_posts` file above, for it to run you need:
  
  >[Python 3.6.8](https://www.python.org/downloads/release/python-368/).
  
  >The PRAW library `pip install praw`.
  
  >The firebase_admin library `pip install firebase_admin`.
  
  >The time library `pip install time`.

  ### Step 3:
  open `filling_the_database_with_posts/therealdoodleishere.py` with a text editor and full up the following:
  ```
  reddit = praw.Reddit(client_id='GIVEN CLIENT ID', \
                     client_secret='YOUR GIVEN USER AGENT SECRET CODE', \
                     user_agent='YOUR USER AGENT USERNAME THAT YOU CREATED', \
                     username='YOUR REDDIT USERNAME', \
                     password='YOUR REDDIT ACCOUNT PASSWORD')
  ```
  >Sadly there's no other way than actually putting your Reddit password that's just how the praw library works (create a throwaway Reddit but it must be the creator of your Reddit application).
  
  ### Step 4:
  go on Firebase and get your `firebase-adminsdk.json`, it can be found here:
  ```
  https://console.firebase.google.com/project/**YOUR_PROJECT_ID**/settings/serviceaccounts/adminsdk
  ```
  and put it in the same folder as the others, and that's it!
  
  Last step: Open a command prompt and cd into the directory where these Python files are and run
  ```
  python this_guy_needs_to_be_run.py
  ```
  you must choose the limit (can't be above 1000 by Reddit limitations).
  
  then choose which display type do you want to pull the posts from (top posts, new posts, controversial posts).
  
  **ALL LOWER CASE**
  and type in your subreddit name (preferably all lower case as when you try to load more pics into existing files in the database with different letter cases it won't be pulled into the same database folder and instead creates a whole new one).
  
  
  #### This will work for your own Facebook Account only as you're the developer, you must submit your app for a review to be live for the public (usually takes ~30mins).
  # That's it!
