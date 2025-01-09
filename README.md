# GitHub Pull Request Fetcher

This script fetches all merged pull requests from specified GitHub repositories and saves their details (PR number, title, body, creation date, and merge date) to a text file. Each repository gets its own `.txt` file named after the repository.

## Features

- Fetch merged pull requests for multiple repositories.
- Save pull request details in a readable format.
- Handles pagination for repositories with many pull requests.

## Requirements

- Python 3.7 or higher
- A GitHub Personal Access Token (PAT) with appropriate permissions:
  - Public repositories: `public_repo`
  - Private repositories: `repo`

## Setup Instructions

### Step 1: Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/shazzad/github-pr-fetcher.git
cd github-pr-fetcher
```

### Step 2: Install Dependencies

Install Python dependencies:

```bash
pip install -r requirements.txt
```

### Step 3: Configure Environment Variables

1. Create a `.env` file in the project directory.
2. Add your GitHub Personal Access Token:
   ```plaintext
   GITHUB_TOKEN=your_personal_access_token
   ```

### Step 4: Update Repository List

Edit the `repos` list in the script to include the repositories you want to fetch pull requests from. For example:

```python
repos = [
    {"owner": "your-username", "repo": "your-repository-name"},
    {"owner": "another-owner", "repo": "another-repo-name"}
]
```

### Step 5: Run the Script

Run the script to fetch pull requests and save them to text files:

```bash
python fetch_pull_requests.py
```

### Step 6: Check Output

For each repository, a `.txt` file will be created in the project directory. The filename will match the repository name (e.g., `your-repository-name.txt`).

---

## Example Output

Here’s an example of what the `.txt` file might look like:

```
PR Number: 1
Title: Fix issue with login
Created At: 2024-01-01T12:00:00Z
Merged At: 2024-01-02T15:00:00Z
Body:
Fixed an issue where users could not log in due to a session timeout problem.

--------------------------------------------------
PR Number: 2
Title: Add new feature for analytics
Created At: 2024-01-05T10:00:00Z
Merged At: 2024-01-06T14:00:00Z
Body:
Implemented a new analytics feature to track user engagement.
```

---

## Troubleshooting

### Error: "Token not provided"

Ensure you’ve created a `.env` file and added your GitHub token as `GITHUB_TOKEN`.

### Error: "403 Forbidden"

This can happen due to:

1. Incorrect or insufficient token permissions.
2. Exceeding the GitHub API rate limit (5,000 requests/hour).

### No Output File Created

Ensure the repository details (`owner` and `repo`) are correct in the `repos` list.

---

## Contributing

Feel free to open issues or submit pull requests to improve this script.

---
