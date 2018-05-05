import os

def get_server_move(image_path, url):
    #nb this is acknowledged as terrible, terrible code
    post_command = ("curl -o response.txt -F 'image=@" +
    image_path + "' " + url)
    os.system(post_command)
    output = ""
    with open("response.txt") as file:
        for line in file:
            output = output + line
    os.remove("response.txt")
    return output

# web test
#print(get_server_move("test/2018-05-03 18-11-43forwards.jpg", "https://snailapi.herokuapp.com/upload"))
# local test
print(get_server_move("test/2018-05-03 18-11-43forwards.jpg", "http://localhost:5000/upload"))
