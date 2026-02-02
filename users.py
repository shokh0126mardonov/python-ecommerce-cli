import json
import hashlib
import os
import uuid

def user_register(username: str, password: str, first_name: str, last_name: str):
    filename = 'users.json'
    if not os.path.exists(filename) or os.path.getsize(filename) == 0:
        users = []
    else:
        with open(filename,'r') as f:
            users = json.load(f)        
    
    for user in users:
        if user['username'] == username:
            print('Bu username allaqachon ro\'yxatdan o\'tgan')
            return
        
    users.append({
        "id":str(uuid.uuid4()),
        "username":username,
        "password":hashlib.sha256(password.encode('utf-8')).hexdigest(),
        "first_name":first_name,
        "last_name":last_name,
        "is_login":False
    })

    with open(filename,'w') as f:
        json.dump(users,f,indent=4)
    
    print("Siz muvaffaqqiyatli ro'yxatdan o'tdingiz!")


def user_login(username:str,password:str):
    filename = 'users.json'
    hash_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    with open(filename) as f:
        users = json.load(f)

        for user in users:
            if user['username'] == username and hash_password == user['password']:
                user['is_login'] = True
                print('Siz login qilindingiz!')
                with open(filename,'w') as f:
                    json.dump(users,f,indent=4)
                return
        
        print('Siz kiritgan username yoki parol xatoxato!')

def user_logout(username:str,password:str):
    filename = 'users.json'
    hash_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    with open(filename) as f:
        users = json.load(f)

        for user in users:
            if username == user['username'] and hash_password == user['password']:
                user['is_login'] = False
                print('Siz logout qilindingiz!')
                with open(filename,'w') as f:
                    json.dump(users,f,indent=4)
                return
        
        print('Logout qilishdan oldin login qilish kerak!')