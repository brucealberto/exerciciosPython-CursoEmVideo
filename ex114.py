from urllib import request, error

try:
    url = request.urlopen("http://www.pudim.com.br")
    # print(url.read())
except error.URLError:
    print("ERROR")
else:
    print("Funcionou")
