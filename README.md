# FaceLife

  When i'm using Free Facebook i don't get to see pictures nor memes outside of only chat messages, so i made this quick chatbot using [Dialogflow](https://dialogflow.com) and [Facebook For Developers](https://developers.facebook.com) and throughout my work i found out you can send an image using its link from [Dialogflow](https://dialogflow.com) to Facebook using the `agent.add()` line in the Fulfillment tab, it will count it as if you've uploaded it and so! you can see it on Free Facebook! here's how you can do it and for free.
  
  It's a two part process:
  1) Setting up Dialogflow:
  Step 1: head on [Dialogflow](https://dialogflow.com) and create a project.
  Step 2: go to the Integrations tab and setup the Facebook Messenger integration ([here's a good tutorial](https://www.youtube.com/watch?v=-2hE3YHsuBQ)).
  Step 2: now you can create intents in the Intent section, we're going to use these to detect what the user is asking us to deliver, and so create a new intent and add a Training Phrase containing a subreddit (for ex. r/tinder), scrolling down to the Fulfillment section click it & check `Enable Web hook call for this intent`, save and exit.
  Step 3: in the Intents list there's a default Fallback Intent, this intent is run everytime our user has typed anything other than the available subreddits, open it & head down to the answer section and select the "Facebook Messenger" tab, remove whatever is in there & add a new Quick reply, this is a menu that will appear in the chat letting the user choose what to quickly type instead of typing it themselves.
