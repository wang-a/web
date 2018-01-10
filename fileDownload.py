import urllib

for i in range(1,1000):
    urllib.urlretrieve('http://test/'+str(i),str(i))
    print i