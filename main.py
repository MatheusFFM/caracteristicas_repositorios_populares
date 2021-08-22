import requests
from datetime import date

headers = {"Authorization": "bearer <Your Token API>"}


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


def save_on_file(query_result):
    result_format = query_result["data"]["search"]["nodes"]
    for rf in result_format:
        today = date.today()
        total_issues = rf["open"]["totalCount"] + rf["closed"]["totalCount"]
        if total_issues == 0:
            total_issues = 1
        created_at = date.fromisoformat(rf["createdAt"][0:10])
        last_update = date.fromisoformat(rf["updatedAt"][0:10])
        delta_created = today - created_at
        delta_updated = today - last_update
        name = rf["nameWithOwner"]
        age_in_days = delta_created.days
        total_pr_accepteds = rf["pullRequests"]["totalCount"]
        total_releases = rf["releases"]["totalCount"]
        last_updated_interval = delta_updated.days
        primary_language = "" if rf["primaryLanguage"] is None else rf["primaryLanguage"]["name"]
        closed_issues_ratio = rf["closed"]["totalCount"] / total_issues


pages = 10
afterCode = None
for page in range(pages):
    print(f"\n========== Page {page + 1} ==========\n")
    result = run_query(afterCode)
    print_query_result(result)
    save_on_file(result)
    has_next = result["data"]["search"]["pageInfo"]["hasNextPage"]
    if not has_next:
        break
    afterCode = result["data"]["search"]["pageInfo"]["endCursor"]
