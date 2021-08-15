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

result = run_query(queryOldRepositories)
print(f"Remaining rate limit - {result}")
