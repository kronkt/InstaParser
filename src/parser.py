import json

class parser():
    #filepaths for followers and following
    followers_json = './json/' + input('followers_json filename:\n')
    following_json = './json/' + input('following_json filename:\n')

    #loading
    with open(followers_json, 'r') as followers_file:
        followers = json.load(followers_file)

    with open(following_json, 'r') as following_file:
        following = json.load(following_file)

    # parsing func (returns set of users within json)
    def parse_json(json_list):
        user_set = set()
        for user in json_list:
            if 'string_list_data' in user:
               for data in user['string_list_data']:
                    user_set.add(data['value'])
            else: print(f"Key 'string_list_data' not found in user: {user}")
        return user_set


    # parsing
    followers_set = parse_json(followers)
    following_set = parse_json(following['relationships_following'])

    not_following_me = following_set - followers_set

    for users in not_following_me:
        print(users)