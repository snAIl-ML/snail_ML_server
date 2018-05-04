import os

def send_stuff(stuff, url):
    post_command = ("curl -o response.txt -F 'image=@" +
    stuff + "' " + url)
    os.system(post_command)
    output = ""
    with open("response.txt") as file:
        for line in file:
            output = output + line
    os.remove("response.txt")
    return output


test = send_stuff(
'/Users/vivianallen/Desktop/Day4InitialModelFiles/test images/2018-05-03 18-11-43forwards.jpg',
'http://localhost:5000/upload'
)

print(test)
print(test)
print(test)
print(test)
print(test)
