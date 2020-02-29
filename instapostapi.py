from instagram_private_api import Client, ClientCompatPatch

email = 'owexactly00@protonmail.com'
password = 'mM9cjG9EpZaATis'

api = Client(email, password)
api.post_photo(photo_data, size, caption='', upload_id=None, to_reel=False, **kwargs)