import requests

# create multiple github repos

def create_repository(repo_name, auth_token):
    url = "https://api.github.com/user/repos"
    headers = {
        "Authorization": f"token {auth_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "name": repo_name,
        "private": False,  # Set to True if you want to create private repositories
        # Add more options like description, homepage, etc., if needed
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print(f"Repository {repo_name} created successfully.")
    else:
        print(f"Failed to create repository {repo_name}. Status code: {response.status_code}")
        print(response.text)

def read_token_from_pem(file_path):
    with open(file_path, 'r') as file:
        token = file.read().strip()
    return token

def main():
    # Replace these values with your GitHub username and path to .pem file
    #username = 'user-name-case-sensitive'
    pem_file_path = './tokenkey'

    # Read token from .pem file
    token = read_token_from_pem(pem_file_path)
    
    # List of repositories to create
    repositories = [
        "repo-1",
        "repo-2",
        "repo-3",

    ]
    
    for repo_name in repositories:
        create_repository(repo_name, token)

if __name__ == "__main__":
    main()