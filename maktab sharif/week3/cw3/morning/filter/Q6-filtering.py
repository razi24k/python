def filter_inappropriate_posts(posts):
    inappropriate_contents = ["fuck", "shit", "shut up", "dick", "cock", "pussy", "fucker"]
    return list(
        filter(lambda post: all(inappropriate_word not in post for inappropriate_word in inappropriate_contents),
               posts))


post_list = ["How can I help you?", "How is your pussy?", "Suck my dick", "You're so lazy"]
print(filter_inappropriate_posts(post_list))
