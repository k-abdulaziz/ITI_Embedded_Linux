import requests

# Your Facebook Access Token with "publish_pages" and "pages_read_engagement" permissions
facebook_access_token = 'paste_token_here'

# Page ID of the Facebook page where you want to post
page_id = 'paste_id_here'

# Post Content as Text
post_message = 'Hello, Facebook! This is my first post using the Facebook Graph API with Python!'

# Post to your Facebook page
post_url = f'https://graph.facebook.com/{page_id}/feed'

payload = {
    'message': post_message,
    'access_token': facebook_access_token,
}

try:
    r = requests.post(post_url, data=payload)
    #r.raise_for_status()
    print('Post was successful! Post ID: {}'.format(r.json()['id']))
except requests.exceptions.HTTPError as err:
    print('Post failed: {}'.format(err))