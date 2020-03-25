from auth import twitter

followers = twitter.followers()
for follower in followers[:1]:
    print(follower)