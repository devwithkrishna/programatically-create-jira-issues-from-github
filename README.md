# programatically-create-jira-issues-from-githu
Programatically create jira issues from Github 

# What code does

* The code leverages `atlassian-python-api`sdk along with python to create jira issues like `Task (Story)`, `Sub Task`, `Epic`

# Parameters required for program

| Argument | Description                                       | Mandatory or not |
| ---------|---------------------------------------------------|------------------|
| type_of_issue | Type of issue like Epic, sub task or story (Task) | ✅ |
| jira_board | In which Jira board you want to create issues     | ✅ |
| epic_key | Epic id if story needs to be attached             | ❌ |
| summary | Issue summary                                     | ✅ |
| description | Issue description                                 | ✅ |
| story_key | Jira story key to attach sub task                 | ❌ |

## Installation (How to use it locally)

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required Python packages:

   * If poetry is not installed locally, do `pip install poetry`  
   
   then, 
      ```bash
      poetry install
      ```
      
   have a look here - https://python-poetry.org/ 

3. Create a `.env` file in the root directory and add your Jira credentials:

    ```plaintext
    JIRA_URL=<your-jira-url>
    JIRA_USERNAME=<your-jira-username>
    JIRA_PASSWORD=<your-jira-password>
    ```
   ##### **_Ensure that your Jira credentials are correctly set in the .env file._**   


## Usage

To run the script, use the following command:

```bash
python <script_name>.py --type_of_issue <issue_type> --jira_board <board_key> --summary <issue_summary> --description <issue_description> [--epic_key <epic_key>] [--story_key <story_key>]
```

## Example Commands
   Create an Epic:

```bash
python create_jira_issue.py --type_of_issue Epic --jira_board BOARD_KEY --summary "Epic Summary" --description "Epic Description"
```

   Create a Task under an Epic:

```bash
python create_jira_issue.py --type_of_issue Task --jira_board BOARD_KEY --epic_key EPIC_KEY --summary "Task Summary" --description "Task Description"
```

   Create a Subtask under a Task:

```bash
python create_jira_issue.py --type_of_issue Subtask --jira_board BOARD_KEY --story_key STORY_KEY --summary "Subtask Summary" --description "Subtask Description"
```