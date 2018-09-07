# !/usr/bin/python
# -*-coding: utf-8 -*-
import sys
from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse

reload(sys)
sys.setdefaultencoding('utf-8')
# from twilio.rest import Client


# account_sid = '***************'
# auth_token = '**************'
# client = Client(account_sid, auth_token)

# call = client.calls.create(
#                         url='http://demo.twilio.com/docs/voice.xml',
#                         to='+86***********',
#                         from_='+***********'
#                     )

# print(call.sid)

app = Flask(__name__)


@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
    """Respond to incoming phone calls with a brief message."""
    # Start our TwiML response
    resp = VoiceResponse()

    # Read a message aloud to the caller
    resp.say(u"4-5失败了", voice='alice', language='zh-CN')

    return str(resp)

@app.route("/voice", methods=['GET', 'POST'])
def voice():
    """Respond to incoming phone calls and mention the caller's city"""
    # Get the caller's city from Twilio's request to our app
    city = request.values['FromCity']

    # Start our TwiML response
    resp = VoiceResponse()

    # Read a message aloud to the caller
    resp.say(u'从不放弃你, {}!'.format(city), voice='alice', language='zh-CN', loop='5')

    # Play an audio file for the caller
    # resp.play('https://demo.twilio.com/docs/classic.mp3')

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)