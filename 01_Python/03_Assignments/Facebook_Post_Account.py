import requests

# Your Facebook Access Token
facebook_access_token = 'paste_token_here'

# Page ID of the Facebook page where you want to post
user_id = 'paste_id_here'

# Post Content as Text
post_message = 'Hello, Facebook! This is my first post using the Facebook Graph API with Python!'

# Privacy settings for the post
privacy_settings = {
    'value': 'SELF' # Set to 'SELF' for a private post visible only to yourself
}

# Post to your Facebook account
post_url = f'https://graph.facebook.com/{user_id}/feed'

payload = {
    'message': post_message,
    'access_token': facebook_access_token,
    'privacy': privacy_settings
}

try:
    r = requests.post(post_url, data=payload)
    r.raise_for_status()
    print('Post was successful! Post ID: {}'.format(r.json()['id']))
except requests.exceptions.HTTPError as err:
    print('Post failed: {}'.format(err))
