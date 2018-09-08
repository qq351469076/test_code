# !/usr/bin/python
# -*-coding: utf-8 -*-
import sys
from twilio.rest import Client

reload(sys)
sys.setdefaultencoding('utf-8')


account_sid = 'ACf8e3298c8fc59eba766626097e9e9303'
auth_token = 'f10fffb0779785a3fb71daf5ec969228'
client = Client(account_sid, auth_token)


call = client.calls.create(
                        url='https://6d90aefa.ngrok.io/2.xml',
                        to='+8618645959590',
                        from_='+14158959590'
                    )



if __name__ == "__main__":
	print(call.sid)