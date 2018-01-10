import urllib

for i in range(1,100):
    urllib.urlretrieve('http://test/'+str(i),str(i))
    print i