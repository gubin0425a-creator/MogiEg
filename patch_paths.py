import os

file_path = 'templates/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('href="/"', 'href="#"')
content = content.replace("onerror=\"this.src='/static/mascot.png'\"", "onerror=\"this.src='static/mascot.png'\"")
content = content.replace('/static/mascot.png', 'static/mascot.png')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Paths patched!')
