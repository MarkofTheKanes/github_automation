import requests

# delete multiple github repos

def delete_repository(repo_owner, repo_name, auth_token):

    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}"
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f"Repository {repo_owner}/{repo_name} deleted successfully.")
    else:
        print(f"Failed to delete repository {repo_owner}/{repo_name}. Status code: {response.status_code}")
        print(response.text)

def read_token_from_pem(file_path):
    with open(file_path, 'r') as file:
        token = file.read().strip()
    return token

def main():
    # Replace these values with your GitHub username and path to .pem file
    username = 'user-name-case-sensitive'
    pem_file_path = './tokenkey'

    # Read token from .pem file
    token = read_token_from_pem(pem_file_path)
    
    # List of repositories to delete
    repositories = [
        "repo-1",
        "repo-2",
        "repo-3",

    ]
    
    for repo_name in repositories:
        delete_repository(username, repo_name, token)

if __name__ == "__main__":
    main()