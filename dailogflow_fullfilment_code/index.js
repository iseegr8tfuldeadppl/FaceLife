'use strict';
 
const functions = require('firebase-functions');
var crypto = require('crypto'),
    	format = require('biguint-format');
const {WebhookClient} = require('dialogflow-fulfillment');
const {Card, Suggestion} = require('dialogflow-fulfillment');

// initialize DB connection
const admin = require('firebase-admin');
admin.initializeApp({
	credential: admin.credential.applicationDefault(),
	databaseURL: 'ws://<your firebase database project>.firebaseio.com/',
});
 
process.env.DEBUG = 'dialogflow:debug'; // enables lib debugging statements
 
exports.dialogflowFirebaseFulfillment = functions.https.onRequest((request, response) => {
  const agent = new WebhookClient({ request, response });
  
  function save(nameParam){
	const { WebhookClient, Image } = require('dialogflow-fulfillment');
    agent.add('Wait for it!');
    const name = nameParam;
    var db = admin.database();
    var rootRef = db.ref();
	var keyRef = rootRef.child(name);
    var obtained_list_of_links = [];
    var obtained_list_of_titles = [];
    var obtained_list_of_selftexts = [];
    return keyRef.once('value').then(snapshot => {
      snapshot.forEach(function(child) {
        var link = child.child("image_source");
        var title = child.child("title");
        var selftext = child.child("selftext");
        obtained_list_of_links.push(link.val());
        obtained_list_of_titles.push(title.val());
        obtained_list_of_selftexts.push(selftext.val());
      });
      var randomer = Math.floor(Math.random()*(obtained_list_of_links.length-1));
      var imaeg = obtained_list_of_links[randomer];
      var titel = obtained_list_of_titles[randomer];
      var selftetx = obtained_list_of_selftexts[randomer];
      if(titel!==''){
        agent.add(titel);
      }
      if(selftetx!==''){
        agent.add(selftetx);
      }
      if(imaeg!==''){
        try{
          agent.add(new Image(imaeg));}
        catch(err){
          console.log(randomer.toString() + " " +imaeg + " " + obtained_list_of_links.length.toString());
        }
      }
      
    });
  }

  function arduinoer(agent){ return save("arduino"); }
  function tinder(agent){ return save("tinder"); }
  function creepypms(agent){ return save("creepypms"); }
  function niceguys(agent){ return save("niceguys"); }
  function pewdiepiesubmissions(agent){ return save("pewdiepiesubmissions"); }
  //add a function for every subreddit like the examples above here ^

  let intentMap = new Map();
  intentMap.set('Arduino', arduinoer);
  intentMap.set('tinder', tinder);
  intentMap.set('creepypms', creepypms);
  intentMap.set('niceguys', niceguys);
  intentMap.set('pewdiepiesubmissions', pewdiepiesubmissions);
  //add a intentmap for every subreddit like the examples above here ^
  
  agent.handleRequest(intentMap);
});
