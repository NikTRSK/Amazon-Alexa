var Alexa = require('alexa-sdk');

exports.handler = function(event, context, callback) {
    var alexa = Alexa.handler(event, context, callback);
}

var handlers = {

    'AboutIntent': function() {
        this.emit(':tell', 'The Red Carpet application has been made by Team1');
    }

};