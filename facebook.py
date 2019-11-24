class Post():
    def __init__(self,text,picture,video):
        self.text=text
        self.picture=picture
        self.video=video

    def post(self):
        global post
        self.posts.append(text)
        print(self.name+"has posted"+text)


class User():
    def __init__(self,name,email,password,friends_list,post):

        self.name=name
        self.email=email
        self.password=password
        self.friends_list=[]
        self.posts=[]
    
    def post(self,text):
        self.text=text
        self.posts.append(text)
        print(self.name+"has posted"+text)

    def get_userinfo(self):
        print("name"+self.name)
        print("email"+self.email)

    def add_friend(self,email):
        self.email=email
        self.friends_list.append(email)
        print(self.name+"has added"+self.email+"as a friend")
 
    def remove_friend(self,email):
        self.email=email
        self.friends_list.remove(email)
        print(self.name+"has removed" +self.email+"as a friend")

    def post(self,text):
        self.text=text
        self.posts.append(text)
        print(self.name+"has posted"+text)
        posts=Post(text,"picture","video")

    def get_userinfo(self):
        print(self.name)
        print(self.email)
        print(self.password)
        print(self.friends_list)
        print("post"+str(self.posts))

Daniel=User("user1","Daniel","Daniel22@meet.mit.edu","ilovemypassword","hi")
Jack=User("user2","Jack","Jack24@meet.mit.edu","whatacoolpassword","cool")
Daniel.add_friend("Jack24@meet.mit.edu")
Jack.post("wasaaaap?")
Daniel.get_userinfo()
Daniel.remove_friend("Jack24@meet.mit.edu")

user=[]
post=[]



   