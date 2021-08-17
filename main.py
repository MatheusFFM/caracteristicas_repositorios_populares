import requests

headers = {"Authorization": "bearer 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"}


def run_query(query):
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))


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

queryOldRepositories  = """
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

queryContributionsRepositories = """
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

queryReleasesRepositories = """
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

queryReleasesRepositories = """
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

queryLastUpdateRepositories = """
{
  search(query: "stars:>100", type: REPOSITORY, first: 100) {
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
  search(query: "stars:>100", type: REPOSITORY, first: 100) {
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

#Get created date of popular repositories.
result = run_query(queryOldRepositories)

Repository = result["data"]["search"]["nodes"]
print("Repositories with its created date.")
for date in Repository: 
  print(date)

print("")
print("///////////////////////////////////////////////////////////////////////////////////////////")
print("")

#Get total pull requests of popular repositories.
result = run_query(queryContributionsRepositories)

Repository = result["data"]["search"]["nodes"]
print("Repositories with number of pull requests")
for date in Repository:
  print(date)

print("")
print("///////////////////////////////////////////////////////////////////////////////////////////")
print("")

#Get total releases of popular repositories.
result = run_query(queryReleasesRepositories)

Repository = result["data"]["search"]["nodes"]
print("Repositories with number of releases")
for date in Repository:
  print(date)

print("")
print("///////////////////////////////////////////////////////////////////////////////////////////")
print("")

#Get last update of popular repositories.
result = run_query(queryLastUpdateRepositories)

Repository = result["data"]["search"]["nodes"]
print("Repositories with number of releases")
for date in Repository:
  print(date)

print("")
print("///////////////////////////////////////////////////////////////////////////////////////////")
print("")

#Get primary language of popular repositories.
result = run_query(queryPrimaryLanguageRepositories)

Repository = result["data"]["search"]["nodes"]
print("Repositories with number of releases")
for date in Repository:
  print(date)




