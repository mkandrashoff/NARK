import csv, re, urllib

class nark():
    def loadlist(self, entitylist):
        self.list=[x for x in csv.reader(open(entitylist, 'r'))]
    def run(self, text):
        self.text=open(text, 'r')
        self.contents=re.split('[^a-z]', self.text.read(), flags=re.IGNORECASE)
        self.contents=set(self.contents)
        self.entityset=[]
        for row in self.list:
            test=set(row)
            if len(test & self.contents)>1:
                self.entityset.append(row[5])
        return self.entityset
    def web_grab(self, url):
        self.text=urllib.urlopen(url)
        self.contents=re.split('[^a-z]', self.text.read(), flags=re.IGNORECASE)
        self.contents=set(self.contents)
        self.entityset=[]
        for row in self.list:
            test=set(row)
            if len(test & self.contents)>1:
                self.entityset.append(row[5])
        return self.entityset
        
        
