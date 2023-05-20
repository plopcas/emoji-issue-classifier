import os
import json
from github import Github

def get_github_client():
    return Github(os.getenv('GITHUB_TOKEN'))

def get_github_repo(client):
    return client.get_repo(os.getenv('GITHUB_REPOSITORY'))

def get_issue_from_event(repo):
    with open(os.getenv('GITHUB_EVENT_PATH')) as f:
        event = json.load(f)
    issue_number = event["issue"]["number"]
    return repo.get_issue(number=issue_number)

def add_label_to_issue(issue, label):
    try:
        existing_label = issue.repository.get_label(label)
    except:
        existing_label = issue.repository.create_label(label, "FFFFFF")
    issue.add_to_labels(existing_label)
    print(f"Added label: {label}")