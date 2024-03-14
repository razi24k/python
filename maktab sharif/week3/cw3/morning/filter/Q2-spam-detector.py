raw_comments = ["nicee", "get rich quick", "so beautiful", "buy now"]
spams = ["buy now", "get rich quick", "visit my profile", "pm for nude"]
filtered_comments = list(filter(lambda comment: comment not in spams, raw_comments))
print(filtered_comments)