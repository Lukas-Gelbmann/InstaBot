from instagram_private_api import Client, ClientCompatPatch
from PIL import Image
import os


username = ''
password = ''
dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path + "/credentials.txt", "r") as credentialFile:
    username = credentialFile.readline()
    password = credentialFile.readline()

picname = '118'


programpath = os.path.dirname(__file__)
path = programpath + '/pictures/' + picname

im = Image.open(path)
width, height = im.size
print(width)
print(height)

with open(path, "rb") as image:
    f = image.read()
    b = bytearray(f)
    print(b[0])
    api = Client(username, password)
    print('now')
    api.post_photo(b, (width, height), caption='lit af', upload_id=None, to_reel=False)