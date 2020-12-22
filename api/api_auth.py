import requests
def get_token():
    api_path = "https://sandboxdnac.cisco.com"
    auth = ("devnetuser","Cisco123!")
    headers = {"Content-type": "application/json"}

    # issue HTTP POST request
    auth_resp = requests.post(f"{api_path}/dna/system/api/v1/auth/token", auth=auth, headers=headers)

    #if succes print token, else raise HTTP error with details
    auth_resp.raise_for_status()
    token = auth_resp.json()["Token"]
    return token

def main():
    token = get_token()
    print(token)


if __name__ == "__main__":
    main()




