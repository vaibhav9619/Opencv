from wit import Wit
access_token="SPK2EB3G3CNXHBKJDNO5VCUZ73XMYFHX"
client=Wit(access_token=access_token)
def wit_res(message_text):
    resp=client.message(message_text)
    entity=None
    value=None
    try:
        entity=list(resp['entities'])[0]
        value=resp['entities'][entity][0]['value']
    except:
        pass
    return (entity,value)


print(wit_res("email address"))
print(wit_res("Delhi"))
print(wit_res("news"))