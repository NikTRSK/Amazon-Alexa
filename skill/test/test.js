var expect = require('chai').expect;
var index = require('../src/index');

const context = require('aws-lambda-mock-context');
const ctx = context();

describe("Testing a session with the LanguageIntent", function() {
    var speechResponse = null
    var speechError = null

    before(function(done) {
        index.handler({
            "session": {
                "sessionId": "SessionId.154291c5-a13f-4e7a-ab5a-707ca12501a8",
                "application": {
                    "applicationId": "amzn1.echo-sdk-ams.app.APP_ID"
                },
                "attributes": {},
                "user": {
                    "userId": null
                },
                "new": true
            },
            "request": {
                "type": "IntentRequest",
                "requestId": "EdwRequestId.474c15c8-14d2-4a77-a4ce-11728a114af7",
                "timestamp": "2016-07-05T22:02:01Z",
                "intent": {
                    "name": "RedCarpetIntent",
                    "slots": {
                        "Brand": {
                            "name": "Brand"
                        },
                        "Events": {
                            "name": "Events",
                            "value": "Oscars"
                        },
                        "Person": {
                            "name": "Person",
                            "value": "Halle berry"
                        }
                    }
                },
                "locale": "en-US"
            },
            "version": "1.0"
        }, ctx)

        ctx.Promise
            .then(resp => {
                speechResponse = resp;
                done();
            })
            .catch(err => {
                speechError = err;
                done();
            })
    })

    describe("The response is structurally correct for Alexa Speech Services", function() {
        console.log(speechResponse)
            // it('should not have errored', function() {
            //     expect(speechError).to.be.null
            // })

        // it('should have a version', function() {
        //     expect(speechResponse.version).not.to.be.null
        // })

        // it('should have a speechlet response', function() {
        //     expect(speechResponse.response).not.to.be.null
        // })

        // it('should have session attributes', function() {
        //     expect(speechResponse.response.sessionAttributes).not.to.be.null
        // })

        // it("should have a spoken response", () => {
        //     expect(speechResponse.response.outputSpeech).not.to.be.null
        // })

        // it("should end the alexa session", function() {
        //     expect(speechResponse.response.shouldEndSession).not.to.be.null
        //     expect(speechResponse.response.shouldEndSession).to.be.true
        // })
    })
})