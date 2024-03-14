files = ["txt.txt", "note.txt", "game of thrones.mp4", "bache nene.mp3", "tree.jpg", "home.png", "rasool.gif"]

images = list(filter(lambda x: x.endswith((".jpg", ".png", "gif")), files))
print(images)
