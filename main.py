import requests

headers = {"Authorization": "bearer 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"}


def run_query(query):
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))


def print_query_result(query_result):
    result_format = query_result["data"]["search"]["nodes"]
    for rf in result_format:
        print(rf)


defaultQuery = """
{
  search(query:"stars>:100", type:REPOSITORY, first:100){
     nodes {
         ... on Repository {
             nameWithOwner
         }
     }
  }
}
"""

query_old_repositories = """
{
  search(query: "stars:>100", type: REPOSITORY, first: 100) {
    nodes {
      ... on Repository {
        nameWithOwner
        createdAt
      }
    }
  }
}
"""

query_contributions_repositories = """
{
  search(query: "stars:>100", type: REPOSITORY, first: 100) {
    nodes {
      ... on Repository {
        nameWithOwner
        pullRequests{
          totalCount
        }
      }
    }
  }
}
"""

query_releases_repositories = """
{
  search(query: "stars:>100", type: REPOSITORY, first: 100) {
    nodes {
      ... on Repository {
        nameWithOwner
        releases{
          totalCount
        }
      }
    }
  }
}
"""


query_last_update_repositories = """
{
  search(query: "stars>:100", type: REPOSITORY, first: 100) {
  nodes {
      ... on Repository {
        nameWithOwner
        updatedAt
      }
    }
  }
}
"""

query_primary_language_repositories = """
{
  search(query: "stars>:100", type: REPOSITORY, first: 100) {
    nodes {
      ... on Repository {
        nameWithOwner
        primaryLanguage{
          name
        }
      }
    }
  }
}
"""

query_closed_issues_from_repositories = """
{ 
  search(query: "stars:>100", type: REPOSITORY, first: 100) {
    nodes {
      ... on Repository {
        nameWithOwner
        issues(states:CLOSED){
          totalCount
        }
      }
    }
  }
}
"""

query_issues_from_repositories = """
{ 
  search(query: "stars:>100", type: REPOSITORY, first: 100) {
    nodes {
      ... on Repository {
        nameWithOwner
        issues {
          totalCount
        }
      }
    }
  }
}
"""


# Get created date of popular repositories.
print("Repositories with its created date.")
print_query_result(run_query(query_old_repositories))
print("\n///////////////////////////////////////////////////////////////////////////////////////////\n")

# Get total pull requests of popular repositories.
print("Repositories with number of pull requests")
print_query_result(run_query(query_contributions_repositories))
print("\n///////////////////////////////////////////////////////////////////////////////////////////\n")

# Get total releases of popular repositories.
print("Repositories with number of releases")
print_query_result(run_query(query_releases_repositories))
print("\n///////////////////////////////////////////////////////////////////////////////////////////\n")

# Get last update of popular repositories.
print("Repositories with last update date")
print_query_result(run_query(query_last_update_repositories))
print("\n///////////////////////////////////////////////////////////////////////////////////////////\n")

# Get primary language of popular repositories.
print("Repositories with primary language")
print_query_result(run_query(query_primary_language_repositories))
print("\n///////////////////////////////////////////////////////////////////////////////////////////\n")

# Get closed issues count of popular repositories.
print("Repositories with count of closed issues")
print_query_result(run_query(query_closed_issues_from_repositories))
print("\n///////////////////////////////////////////////////////////////////////////////////////////\n")

# Get total issues count of popular repositories.
print("Repositories with count of issues")
print_query_result(run_query(query_issues_from_repositories))
print("\n///////////////////////////////////////////////////////////////////////////////////////////\n")
