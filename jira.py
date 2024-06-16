import os
import argparse
from dotenv import load_dotenv
from atlassian import Jira
from date_time import date_time


def create_story_under_epic(epic_key: str, summary:str, description:str, jira_board:str):
    """
    create a story (Task) attaching it to a specific epic
    :param epic_key:
    :param summary:
    :param description:
    :param jira_board:
    :return:
    """
    # Initialize Jira
    JIRA_URL = os.getenv('JIRA_URL')
    JIRA_USERNAME = os.getenv('JIRA_USERNAME')
    JIRA_PASSWORD = os.getenv('JIRA_PASSWORD')
    jira = Jira(url=os.getenv('JIRA_URL'), username=os.getenv('JIRA_USERNAME'), password=os.getenv('JIRA_PASSWORD'),
                cloud=True)

    issue_dict = {
        'project': {'key': jira_board },
        'summary': summary,
        'description': description,
        'issuetype': {'name': 'Task'},
        'parent': {
            "key": epic_key
        }
    }
    new_issue = jira.issue_create(fields=issue_dict)

    return new_issue

def create_epic(summary:str, description:str, jira_board:str):
    """
    Create an Epic under a specific Jira board
    :param summary:
    :param description:
    :param jira_board:
    :return:
    """
    # Initialize Jira
    JIRA_URL = os.getenv('JIRA_URL')
    JIRA_USERNAME = os.getenv('JIRA_USERNAME')
    JIRA_PASSWORD = os.getenv('JIRA_PASSWORD')
    jira = Jira(url=os.getenv('JIRA_URL'), username=os.getenv('JIRA_USERNAME'), password=os.getenv('JIRA_PASSWORD'),
                cloud=True)

    issue_dict = {
        'project': {'key': jira_board },
        'summary': summary,
        'description': description,
        'issuetype': {'name': 'Epic'}
    }
    new_issue = jira.issue_create(fields=issue_dict)

    return new_issue


def create_subtask_under_story( summary:str, description:str, jira_board:str, story_key:str):
    """
    Create a sub task on a Jira story
    :param summary:
    :param description:
    :param jira_board:
    :param story_key:
    :return:
    """
    # Initialize Jira
    JIRA_URL = os.getenv('JIRA_URL')
    JIRA_USERNAME = os.getenv('JIRA_USERNAME')
    JIRA_PASSWORD = os.getenv('JIRA_PASSWORD')
    jira = Jira(url=os.getenv('JIRA_URL'), username=os.getenv('JIRA_USERNAME'), password=os.getenv('JIRA_PASSWORD'),
                cloud=True)

    issue_dict = {
        'project': {'key': jira_board },
        'summary': summary,
        'description': description,
        'issuetype': {'name': 'Subtask'},
        'parent': {
            "key": story_key
        }
    }
    new_issue = jira.issue_create(fields=issue_dict)

    return new_issue


def main():
    """testing script"""
    # Initializing jira client
    load_dotenv()
    parser = argparse.ArgumentParser("Programatically create Jira Issues")
    parser.add_argument("--type_of_issue", help="Type of Jira issue to be created", choices=["Epic", "Task", "Subtask"], required=True)
    parser.add_argument("--jira_board", help="Your Jira board Key", required=True, type=str)
    parser.add_argument("--epic_key", help="Jira EPIC id to attach issue", required=False, type=str)
    parser.add_argument("--summary", help="Issue summary", required=True, type=str)
    parser.add_argument("--description", help="Issue description", required=True, type=str)
    parser.add_argument("--story_key", help="Jira story key to attach sub task", type=str, required=False)

    args = parser.parse_args()
    jira_board = args.jira_board
    epic_key = args.epic_key
    summary = args.summary
    description = args.description
    story_key = args.story_key
    type_of_issue = args.type_of_issue

    if type_of_issue == 'Epic':
        # Create Epic
        epic = create_epic(summary, description, jira_board)
        print(f"Created Epic {epic['key']} on jira board {jira_board} at {date_time()} IST")
    elif type_of_issue == "Task":
        if not epic_key:
            raise ValueError("epic_key is required for creating a Task")
        # Create the story attaching to an epic
        story = create_story_under_epic(epic_key, summary, description, jira_board)
        print(f"Created story {story['key']} with epic {epic_key} at {date_time()} IST")
    else:
        if not story_key:
            raise ValueError("story_key is required for creating a Subtask")
        # Create Sub task under a story
        sub_task = create_subtask_under_story(summary, description, jira_board, story_key=story_key)
        print(f"Created story {sub_task['key']} under epic {epic_key} at {date_time()} IST")



if __name__ == "__main__":
    main()