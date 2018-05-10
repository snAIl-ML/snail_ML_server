'Module to get commands for directions'
import requests

def get_server_move(image_path, url):
    'Function to obtain command'
    server_move = requests.post(url, files={'image': open(image_path, 'rb')})
    return server_move.text

# web test (uncomment and join the next 2 lines to see the web test (pylint))
# print(get_server_move("test/2018-05-03 18-11-43forwards.jpg",
# "https://snailapi.herokuapp.com/upload"))
# local test
print(get_server_move("test/2018-05-03 18-11-43forwards.jpg", "http://localhost:5000/upload"))
