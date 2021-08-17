import sys
import base64
import rest


client_id = sys.argv[1]
client_secret = sys.argv[2]


def get_token(i, s):
    url = 'https://visibility.amp.cisco.com/iroh/oauth2/token'
    b64 = base64.b64encode((i + ':' + s).encode()).decode()
    header = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'Authorization': 'Basic ' + b64
    }
    payload = 'grant_type=client_credentials'
    response = rest.post(url, header, payload)
    if response:
        return response['access_token']


def get_incidents(token, search):
    base_url = 'https://intel.amp.cisco.com/ctia/incident/search'
    url = base_url + '?' + search
    header = {
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + token
    }
    return rest.get(url, header)


def delete_incident_query(token, search):
    base_url = 'https://intel.amp.cisco.com/ctia/incident/search'
    url = base_url + '?' + search
    header = {
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + token
    }
    return rest.delete(url, header)


def delete_incident_id(token, id):
    base_url = 'https://intel.amp.cisco.com/ctia/incident/'
    url = base_url + str(id)
    header = {
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + token
    }
    return rest.delete(url, header)


token = get_token(client_id, client_secret)
query = 'sort_order=desc&limit=100'
incidents = get_incidents(token, query)
print('hi')