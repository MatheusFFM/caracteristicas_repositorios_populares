import requests

headers = {"Authorization": "bearer <your git token>"}


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


repositories_query = """
{
  search(query:"stars>:100", type:REPOSITORY, first:100){
     nodes {
         ... on Repository {
             nameWithOwner
             url
             stargazers {
                totalCount
             }
             createdAt
             pullRequests(states:MERGED) {
                totalCount
             }
             releases {
                totalCount
             }
             updatedAt
             primaryLanguage{
                name
             }
             open: issues(states:OPEN) {
                totalCount
             }
             closed: issues(states:CLOSED) {
                totalCount
             }
         }
     }
  }
}
"""


# Get data of popular repositories.
print("Popular repositories data")
print_query_result(run_query(repositories_query))
print("\n///////////////////////////////////////////////////////////////////////////////////////////\n")
