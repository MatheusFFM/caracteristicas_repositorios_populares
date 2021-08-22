import requests

headers = {"Authorization": "bearer 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"}


def run_query(after):
    after_formatted = "null" if after is None else "\"" + after + "\""
    query = """
    {
      search(query:"stars:>100", type:REPOSITORY, first:100, after:""" + after_formatted + """){
        pageInfo {
            endCursor
            hasNextPage
        } 
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
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))


def print_query_result(query_result):
    result_format = query_result["data"]["search"]["nodes"]
    for rf in result_format:
        print(rf)


pages = 10
afterCode = None
for page in range(pages):
    print(f"\n========== Page {page+1} ==========\n")
    result = run_query(afterCode)
    print_query_result(result)
    has_next = result["data"]["search"]["pageInfo"]["hasNextPage"]
    if not has_next:
        break
    afterCode = result["data"]["search"]["pageInfo"]["endCursor"]
