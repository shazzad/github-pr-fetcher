import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}

# List of repositories to fetch PR data from
repos = [
    # Add more repositories as needed
    {"owner": "your-username", "repo": "your-repository-name"},
]

# GraphQL query to fetch pull requests
query = """
query ($owner: String!, $repo: String!, $cursor: String) {
repository(owner: $owner, name: $repo) {
	pullRequests(states: MERGED, first: 100, after: $cursor) {
	nodes {
		title
		body
		createdAt
		mergedAt
		number
	}
	pageInfo {
		endCursor
		hasNextPage
	}
	}
}
}
"""

# Loop through each repository
for repo in repos:
    variables = {"owner": repo["owner"], "repo": repo["repo"], "cursor": None}
    has_next_page = True
    repo_name = repo["repo"]

    # Open a file named after the repository to write PR content
    with open(f"{repo_name}.txt", "w", encoding="utf-8") as file:
        while has_next_page:
            # Make a request to the GitHub GraphQL API
            response = requests.post(
                "https://api.github.com/graphql",
                json={"query": query, "variables": variables},
                headers=headers,
            )
            data = response.json()

            # Handle potential errors
            if "errors" in data:
                print(f"Error fetching data for {repo_name}: {data['errors']}")
                break

            # Extract PR data
            pr_data = data["data"]["repository"]["pullRequests"]["nodes"]

            # Write PR content to the file
            for pr in pr_data:
                file.write(f"PR Number: {pr['number']}\n")
                # file.write(f"Title: {pr['title']}\n")
                # file.write(f"Created: {pr['createdAt']}\n")
                # file.write(f"Body:\n{pr['body']}\n")
                # file.write("-" * 50 + "\n")
                if pr["body"]:
                    file.write(f"{pr['body']}\n")
                else:
                    file.write(f"{pr['title']}\n")

            # Handle pagination
            page_info = data["data"]["repository"]["pullRequests"]["pageInfo"]
            has_next_page = page_info["hasNextPage"]
            variables["cursor"] = page_info["endCursor"]

print("Pull request content saved to text files.")
