import json

#filepaths for followers and following
followers_json = './json/followers_1.json'
following_json = './json/following.json'

#loading
with open(followers_json, 'r') as followers_file:
    followers = json.load(followers_file)

with open(following_json, 'r') as following_file:
    following = json.load(following_file)

def parse_json(json_file):
    user_set = set()
    for user in json_file:
        if 'string_list_data' in user:
           for data in user['string_list_data']:
                user_set.add(data['value'])
        else: print(f"Key 'string_list_data' not found in user: {user}")
    return user_set

# parsing
followers_set = parse_json(followers)
following_set = parse_json(following)

not_following_me = followers_set - following_set

for users_not_following in not_following_me:
    print(users_not_following)