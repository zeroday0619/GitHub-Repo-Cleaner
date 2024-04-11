import os
from github import Github
from github.Auth import Login


auth = Login("token", os.getenv("GITHUB_TOKEN"))
gh = Github(auth=auth)
for repo in gh.get_user(os.getenv("GITHUB_USERNAME")).get_repos():
    if repo.fork:
        match repo.name:
            case "PyGithub" | "XenXenXenSe" | "XenGarden" | "uvloop":
                pass
            case _:
                print(repo.name)
                print(repo.edit_ownersip(new_owner=""))