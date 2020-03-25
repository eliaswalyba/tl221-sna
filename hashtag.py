from auth import twitter
import json

search_results = twitter.search(q="COVID19sn")
for result in search_results[:1]:
    # json_str = json.dumps(result._json)
    # parsed = json.loads(json_str)
    # print(json.dumps(parsed, indent=4, sort_keys=True))
    replies = twitter.search(q=f"to:{result.user.screen_name}", sinceId=result.id)
    quotes = twitter.search(q=f"-from:quotedreplies url:{result.id}")
    print(f"Tweet = {result.text}")
    print(f"User  = {result.user.screen_name}")
    print(f"Number of replies = {len(replies)}")
    print(f"Number of quotes  = {len(quotes)}")