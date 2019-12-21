import webbrowser
class shortenurl:
    url={}
    id=1000000
    def short(self,original):
        if original in self.url:
            id=self.url[original]
            shorturl=id
        else:
            self.url[original]=self.id
            shorturl=self.id
            self.id +=1
        print("short url: ",'tinyurl./'+str(shorturl))
    
        return self.url

a=input("Enter the url : ")
b=shortenurl()
c=b.short(a)
print("\n")
url2=input("Enter shoturl to get original : ")
url3=url2.split("/")
insert=int(url3[1])
for key in c:
    if c[key] == insert:
        a=key
        print("The original url is: ",key)
webbrowser.open(a)
