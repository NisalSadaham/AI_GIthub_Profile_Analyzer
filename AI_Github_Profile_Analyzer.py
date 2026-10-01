import requests
from google import genai
from dotenv import load_dotenv
import os
import json

load_dotenv()



def fetch(username):
    url = f"https://api.github.com/users/{username}"

    try:
        response = requests.get(url,timeout=5)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 401:
            print("Authentication failed")
        elif e.response.status_code == 403:
            print("Access forbidden")
        elif e.response.status_code == 404:
            print("Resource not found")
        elif e.response.status_code == 429:
            print("Rate limit exceeded")
        else:
            print("Error:",e)
    except requests.exceptions.RequestException as e:
        print(e)
def fetch_repos(username):
        url = f"https://api.github.com/users/{username}/repos"
    
        try:
            response = requests.get(url,timeout=5)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            print(e)

def get_ai_summary(profile_for_ai):
    try:
        api_key = os.getenv("GEMINI_API_KEY")
        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
        model= "gemini-3.1-flash-lite",
        contents= f"Analyze the following public GitHub profile data {profile_for_ai}.Give a concise summary of the developer's profile and repositories.Do not invent information that isn't present in the data.")
    except Exception as e:
        print("Error:",e)
        return None

    return response.text
def main():
    while True:
        username = input("Enter github username to get info:")
        data = fetch(username=username)
        if data is not None:
            repos = fetch_repos(username= username)
            print("Username:",data["login"])
            print("Bio:",data["bio"])
            print("ID:",data["id"])
            print("Following:",data["following"])
            print("Followers:",data["followers"])
            print("public_repos:",data["public_repos"])

            if repos is not None:
                repo_list = []
                print("=========Repo list========")
                for repo in repos:
                    repo_list.append(repo["name"])
                    print("Repo_Name:",repo["name"])
                print("===========================")
            else:
                print("Repo is empty")

            profile_for_ai = {
                "UserName":data["login"],
                "Bio":data["bio"],
                "repositories":repo_list
            }
            json_version = json.dumps(profile_for_ai)
            ai_summary = get_ai_summary(json_version)

            if ai_summary  is not None:
                print("Account Summary:",ai_summary)
            else:
                print("Summary was not generated..")
                        
            _continue= input("Do you want to search another user(y/n)").lower()
            if _continue == "y":
                continue
            elif _continue == "n":
                print("exiting system...")
                break
            else:
                print("Invalid input")
                continue

        else:
            print("Sorry couldnt fetch information")
            

        

main()