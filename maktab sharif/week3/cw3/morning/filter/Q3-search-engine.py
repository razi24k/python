def filter_irrelevant_results(search_results, search_keywords):
    keywords_list = search_keywords.split(" ")
    return list(filter(lambda result: any(keyword in result for keyword in keywords_list), search_results))


search_res = ["cheap computer", "nice computer", "computer", "laptop", "compose", "cheap laptop"]
keywords = "cheap computer"
print(filter_irrelevant_results(search_res, keywords))

