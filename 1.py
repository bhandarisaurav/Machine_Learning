from easygui import passwordbox, ynbox
import easygui

password = None
x = ynbox('Shall I continue?', 'Title', ['Yes', 'No'])
if x:
    password = passwordbox("PASSWORD:")
print(password)
print(easygui.buttonbox('Click on your favorite flavor.', 'Favorite Flavor', ['Chocolate', 'Vanilla', 'Strawberry']))

reply = easygui.buttonbox("Choose: ", image="image.jpg", choices=['Open', 'Close', 'Exit'])
print(reply)