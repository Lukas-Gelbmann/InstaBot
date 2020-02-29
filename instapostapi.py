from instagram_private_api import Client, ClientCompatPatch
import os


email = 'owexactly00@protonmail.com'
password = 'mM9cjG9EpZaATis'
picname = '1'


programpath = os.path.dirname(__file__)
path = programpath + '/pictures/' + picname + '.jpg'

with open(path, "rb") as image:
    f = image.read()
    b = bytearray(f)
    print(b[0])


api = Client(email, password)
api.post_photo(photo_data, size, caption='lit af', upload_id=None, to_reel=False)