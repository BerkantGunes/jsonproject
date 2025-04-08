import json
import os

class User:
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currenctUser = {}

        # load users from json file
        self.loadUsers()

    def loadUsers(self):
        if os.path.exists('users.json'):
            with open('users.json','r') as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    newUser = User(username = user['username'], password= user['password'], email = user['email'])
                    self.users.append(newUser)

            print(self.users)

    def register(self, user:User): #register fonksiyonu
        self.users.append(user)
        self.savetoFile()
        print('Kullanici olusturuldu.')
    def login(self,username,password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print('Login yapildi.')
                break

    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print('Cikis yapildi')

    def identity(self):
        if self.isLoggedIn:
            print(f'username: {self.currentUser.username}')
        else:
            print('Giris yapilamadi!')

    def savetoFile(self):
        list = []

        for user in self.users:
            list.append(json.dumps(user.__dict__)) # user classini (username,password,email verilerini)tamamen dictionary yapisina cevirir

        with open('users.json','w') as file:
            json.dump(list, file)

repository = UserRepository()

while True:
    print('Menu'.center(50,'*'))
    secim = input('1- Register\n2- Login\n3- Logout\n4- identity\n5- Exit\nseciminiz: ')
    if secim == '5':
        break

    else:
        if secim == '1':
            username = input('username: ')
            password = input('password: ')
            email = input('email: ')

            user = User(username = username, password = password, email = email)
            repository.register(user)

            print(repository.users)

        elif secim == '2':
            #login
            if repository.isLoggedIn:
                print('Zaten Login oldunuz!')
            else:
                username = input('username: ')
                password = input('password: ')

                repository.login(username,password)
        elif secim == '3':
            #logout
            repository.logout()
        elif secim == '4':
            # display username
            repository.identity()
        else:
            print('yanlis secim')
