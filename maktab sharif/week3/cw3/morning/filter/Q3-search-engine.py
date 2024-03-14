def filter_irrelevant_results(search_results, search_keywords):
    searches = []
    for i in search_results:
        res = i.split(" ")
        searches.append(res)
    return list(filter(lambda result: any(x in result for x in search_keywords), searches))


search_res = ["cheap computer", "nice computer", "computer", "laptop", "compose"]
keywords = ["computer", "laptop"]
print(filter_irrelevant_results(search_res, keywords))
