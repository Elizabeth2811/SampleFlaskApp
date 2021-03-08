userlist =[{'name':'XYZ','location':'LA'},{'name':'ABC','location':'NZ'}]

def addUser(user_info):
    userlist.append(user_info)
    return userlist

def deleteUser(user_name):
    
    del_li = []

    for cnt, user_li in enumerate(userlist):
        if  user_li['name'] == user_name:
            del_li.append(cnt) 
    for delid in del_li:
        userlist.pop(delid)

    return                    

def getUser():
    return userlist    
            
