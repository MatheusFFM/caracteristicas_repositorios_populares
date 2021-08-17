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
  search(query:"stars", type:REPOSITORY, first:100){
     nodes {
         ... on Repository {
             nameWithOwner
         }
     }
  }
}
"""

queryOldRepositories = """
{
  search(query: "stars", type: REPOSITORY, first: 100) {
    nodes {
      ... on Repository {
        nameWithOwner
        createdAt
      }
    }
  }
}
"""

queryContributionsRepositories = """
{
  search(query: "stars", type: REPOSITORY, first: 100) {
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

queryReleasesRepositories = """
{
  search(query: "stars", type: REPOSITORY, first: 100) {
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

queryReleasesRepositories = """
{
  search(query: "stars", type: REPOSITORY, first: 100) {
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

queryLastUpdateRepositories = """
{
  search(query: "stars", type: REPOSITORY, first: 100) {
  nodes {
      ... on Repository {
        nameWithOwner
        updatedAt
      }
    }
  }
}
"""

queryPrimaryLanguageRepositories = """
{
  search(query: "stars", type: REPOSITORY, first: 100) {
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

queryPrimaryLanguageRepositories = """
{
  search(query: "stars", type: REPOSITORY, first: 100) {
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

# Get created date of popular repositories.
print("Repositories with its created date.")
print_query_result(run_query(queryOldRepositories))
print("\n///////////////////////////////////////////////////////////////////////////////////////////\n")

# Get total pull requests of popular repositories.
print("Repositories with number of pull requests")
print_query_result(run_query(queryContributionsRepositories))
print("\n///////////////////////////////////////////////////////////////////////////////////////////\n")

# Get total releases of popular repositories.
print("Repositories with number of releases")
print_query_result(run_query(queryReleasesRepositories))
print("\n///////////////////////////////////////////////////////////////////////////////////////////\n")

# Get last update of popular repositories.
print("Repositories with last update date")
print_query_result(run_query(queryLastUpdateRepositories))
print("\n///////////////////////////////////////////////////////////////////////////////////////////\n")

# Get primary language of popular repositories.
print("Repositories with primary language")
print_query_result(run_query(queryPrimaryLanguageRepositories))
print("\n///////////////////////////////////////////////////////////////////////////////////////////\n")