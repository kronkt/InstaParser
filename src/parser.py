import json
import sys # for any exceptions

class UserParser():

    def __init__(self, followers_json_path, following_json_path):
        # load followers and following data during initialization
        self.followers = self._load_json(followers_json_path)

        # .get() returns the values associated with the key 'relationships_following' aka 'value'. 
        # Otherwise returns empty list (if 'relationships_following' key can't be found).
        self.following = self._load_json(following_json_path).get('relationships_following', [])

    # private method (_in_front_of_method_name)
    def _load_json(self, file_path):
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            # 2 different exceptions in a tuple, will catch either of these (doesn't have to be both)
            # if file doesn't exist, will invoke 'FileNotFoundError'
            # if json format isn't valid, will invoke 'json.JSONDecodeError'
            print(f"Error loading {file_path}: {e}")
            # exit program if exceptions have been met
            return sys.exit(1)

    def parse_usernames(self, json_list):
        # parses usernames from list and returns them as a set
        user_set = set()
        for user in json_list:
            # accessing 'string_list_data' within each user(if it exists)
            if 'string_list_data' in user:
               for data in user['string_list_data']:
                    user_set.add(data['value']) # extracting 'value' field
            else: print(f"Key 'string_list_data' not found in user: {user}")
        return user_set


    def not_following_me(self):
        # finds users who don't follow you back
        followers_set = self.parse_usernames(self.followers)
        following_set = self.parse_usernames(self.following)
        not_following_back = following_set - followers_set
        return not_following_back
        

    def print_not_following_me(self):
        # print each instant of user who doesn't follow you back
        not_following_back = self.not_following_me()
        print("\nUsers who don't follow you back:\n")
        for user in not_following_back:
            print(user)

    def count_not_following_me(self):
        # get set of users who don't follow back
        not_following_back = self.not_following_me()

        # count
        total = len(not_following_back)
        print(f"\nTotal number of users who don't follow you back: {total}")

            
if __name__ == "__main__":
    # filepaths for followers and following given by end user
    followers_file = './json/' + input('followers_json filename:\n')
    following_file = './json/' + input('following_json filename:\n')

    user_parser = UserParser(followers_file, following_file)
    user_parser.print_not_following_me()
    user_parser.count_not_following_me()
