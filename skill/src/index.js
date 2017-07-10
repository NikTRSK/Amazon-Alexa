/*
    Quick sample for the Amazon Alexa RedCarpet skill app
*/
'use strict';

const Alexa = require('alexa-sdk');
var Data = require("./data.json");

const APP_ID = 'amzn1.ask.skill.c06dcf1c-6929-410c-ac06-2970bb87f04b'; // TODO replace with your app ID (OPTIONAL).

// const Data = {
//     "oscars": [{
//             "description": "In Versace",
//             "title": "Halle Berry",
//             "url": "http://akns-images.eonline.com/eol_images/Entire_Site/2017126/rs_634x1024-170226165902-634-academy-awards-oscars-2017-arrivals-halle-berry.jpg"
//         },
//         {
//             "description": "In Narciso Rodriguez",
//             "title": "Kate McKinnon",
//             "url": "http://akns-images.eonline.com/eol_images/Entire_Site/2017126/rs_634x1024-170226170353-634-kate-mckinnon.cm.22617.jpg"
//         }
//     ],
//     "people's choice awards": [{
//             "description": "&nbsp;We\"ve been waiting for tonight to see the <em>Shades of Blue</em> star pull off another winning look. Spoiler: She didn\"t disappoint in her&nbsp;black gown with a sheer beaded bust by Reem Acra and&nbsp;Salvatore Ferragamo clutch.",
//             "title": "Jennifer Lopez",
//             "url": "http://akns-images.eonline.com/eol_images/Entire_Site/2017018/rs_634x1024-170118174219-634-jennifer-lopez-peoples-choice-awards-2017.jpg"
//         },
//         {
//             "description": "Before their highly anticipated performance, Ally Brooke, Normani Kordei, Lauren Jauregui and Dinah Jane prove to be the perfect match.&nbsp;",
//             "title": "Fifth Harmony",
//             "url": "http://akns-images.eonline.com/eol_images/Entire_Site/2017018/rs_839x1024-170118174826-634-fifth-harmony-peoples-choice-awards-2017.jpg"
//         }
//     ]
// };

const skillName = "Red Carpet";

var handlers = {

    "RedCarpetIntent": function() {
        var speechOutput = "";
        // Get the slot value
        var slot_type = this.event.request.intent.slots.Events;
        var person_slot = this.event.request.intent.slots.Person;
        if (!slot_type)
            speechOutput = "I don't have anything interesting to share regarding what you've asked.";
        else {
            var eventName = this.event.request.intent.slots.Events.value.toLowerCase();
            var eventData = Data[eventName];
            if (eventData) {
                var outfit = eventData.find((item) => {
                    return item.title.toLowerCase() == person_slot.value.toLowerCase();
                });
                if (outfit)
                    speechOutput += "At the " + eventName + ", " + eventData.title +
                    " wore " + eventData.description;
                else
                    speechOutput = person_slot.value + " didn't attend " + eventName;
            } else {
                speechOutput = "I don't have anything interesting to share regarding what you've asked."
            }
        }
        this.emit(':tellWithCard', speechOutput, skillName, speechOutput);
    },

    "AboutIntent": function() {
        var speechOutput = "The Polyglot Developer, Nic Raboy, is from San Francisco, California";
        this.emit(':tellWithCard', speechOutput, skillName, speechOutput);
    },

    "AMAZON.HelpIntent": function() {
        var speechOutput = "";
        speechOutput += "Here are some things you can say: ";
        speechOutput += "Tell me something interesting about Java. ";
        speechOutput += "Tell me about the skill developer. ";
        speechOutput += "You can also say stop if you're done. ";
        speechOutput += "So how can I help?";
        this.emit(':ask', speechOutput, speechOutput);
    },

    "AMAZON.StopIntent": function() {
        var speechOutput = "Goodbye";
        this.emit(':tell', speechOutput);
    },

    "AMAZON.CancelIntent": function() {
        var speechOutput = "Goodbye";
        this.emit(':tell', speechOutput);
    },

    'Unhandled': function() {
        this.emit(':ask', 'Insert your own error message here');
    },

    "LaunchRequest": function() {
        var speechText = "";
        speechText += "Welcome to " + skillName + ".  ";
        speechText += "You can ask a question like, tell me something interesting about Java.  ";
        var repromptText = "For instructions on what you can say, please say help me.";
        this.emit(':ask', speechText, repromptText);
    }

};

exports.handler = function(event, context) {
    var alexa = Alexa.handler(event, context);
    alexa.APP_ID = APP_ID;
    // alexa.appId = "amzn1.echo-sdk-ams.app.APP_ID";
    alexa.registerHandlers(handlers);
    alexa.execute();
};