file = open('cartoon.png','rb')
data = file.read()
file.close()
file = open('cartoon_2.png','wb')
file.write(data)
file.close()
