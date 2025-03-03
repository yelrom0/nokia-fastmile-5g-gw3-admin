from auth import auth
from settings import get_settings

# load settings from .env
settings = get_settings()

# auth with router
login_data, sess = auth()

if login_data['result'] != 0:
        raise Exception(f"Nokia Modem Login Error\n\nData\n----\n\n{login_data}")

data = {'csrf_token': login_data['token']}

resp = sess.post(f"http://{settings.router_ip}//reboot_web_app.cgi", data=data)
first_line = resp.text.split("\n")[0]

if first_line != "Enter reboot cgi Initialize function":
        print(first_line)
        print(resp.text)
else:
        print('Nokia Modem Success - Rebooting')
# {"result":0,"sid":"wjbNrlRXCmdzuadN","token":"fGiFvSmIuXsriHvq"}
# csrf_token: fGiFvSmIuXsriHvq
# csrf_token == token
# cookie: sid=wjbNrlRXCmdzuadN
# Response below
# Enter reboot cgi Initialize function
# l_host = 169.254.250.1, l_port = 1883 
# Client mosq-kSevhmvMOpRxecHcqR sending CONNECT
# Client mosq-kSevhmvMOpRxecHcqR received CONNACK (0)
# Client mosq-kSevhmvMOpRxecHcqR sending SUBSCRIBE (Mid: 1, Topic: /MaintenanceAction/SyncRequest, QoS: 2, Options: 0x00)
# connect success
# Client mosq-kSevhmvMOpRxecHcqR received SUBACK
# subscribe_callback thread pid 22945
# Successed to start a thread for restart Client mosq-kSevhmvMOpRxecHcqR sending PUBLISH (d0, q2, r0, m2, '/MaintenanceAction/Request', ... (181 bytes))
# pub message topic = /MaintenanceAction/Request, data = 
#  { "MessageID": "MaintenanceActionRequest", "MessageSender": "Web", "MessageSequence": 1, "Content": { "Action": "RebootSystem", "Originator": "Web", "RootCause": "WEBGUI Reboot" } } 
# Client mosq-kSevhmvMOpRxecHcqR received PUBREC (Mid: 2)
# Client mosq-kSevhmvMOpRxecHcqR sending PUBREL (m2)
# Client mosq-kSevhmvMOpRxecHcqR received PUBCOMP (Mid: 2, RC:0)
# Client mosq-kSevhmvMOpRxecHcqR received PUBLISH (d0, q2, r0, m1, '/MaintenanceAction/SyncRequest', ... (212 bytes))
# Client mosq-kSevhmvMOpRxecHcqR sending PUBREC (m1, rc0)
# Client mosq-kSevhmvMOpRxecHcqR received PUBREL (Mid: 1)
# Client mosq-kSevhmvMOpRxecHcqR sending PUBCOMP (m1)
# my_message_callback call topic is /MaintenanceAction/SyncRequest, thread id is 22945
# receive topic /MaintenanceAction/SyncRequest,  message payload is { "MessageID": "MaintenanceActionSyncRequest", "MessageSender": "HAMgr", "MessageSequence": 9, "Content": { "Action": "RebootSystem", "Originator": "Web", "RequestMSGSequence": 1, "RootCause": "WEBGUI Reboot" } }
# X-Frame-Options:SAMEORIGIN
# X-Content-Type-Options:nosniff
# X-XSS-Protection:1; mode=block
# Content-Security-Policy:default-src 'self'; frame-ancestors 'self'; form-action 'self'
# Strict-Transport-Security:max-age=7776000; includeSubdomains
# Content-type:text/html;charset=UTF-8

