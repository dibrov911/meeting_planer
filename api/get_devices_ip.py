import requests
from api_auth import get_token

def main():
    token = get_token()
    api_path = "https://sandboxdnac.cisco.com"
    #print(token)
    headers = {"Contet-type":"application/json", "X-Auth-Token":token}
    get_resp = requests.get(f"{api_path}/dna/intent/api/v1/network-device",headers=headers)
    get_resp.raise_for_status()
    
#   Debugging output
    import json
    print(get_resp.json()["response"])
    
    if get_resp.ok: 
        for device in get_resp.json()["response"]:
            print(f"ID: {device['id']} IP: {device['managementIpAddress']}")
    else: 
        print('Device collection failed')

if __name__ == "__main__":
   main()