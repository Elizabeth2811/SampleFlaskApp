from flask import Flask,request,jsonify
import flaskapp.user_info as user_info
app = Flask(__name__)

@app.route('/add',methods=['POST'])
def postdata():
    new_user = request.get_json()
    user_list  = user_info.addUser(new_user)
    return jsonify({"flag":user_list[-1]})

@app.route('/get',methods=['GET'])
def getdata():
    return jsonify(user_info.getUser())

@app.route('/delete',methods=['Delete'])
def delete():
    uname = request.get_json()['name']
    
    user_info.deleteUser(uname)
    return "Deleted"


if __name__=='__main__':
    app.run('0.0.0.0',5001,debug=False)    

    