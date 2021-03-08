import sys,json, pytest,os
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/..")
#base_path=os.getcwd()
#parser.read(os.path.join(base_path,'config.ini'))
#sys.path.append(os.path.join('../',base_path))
from app import app


def test_getdata(client):
    response = client.get('/get')
    assert response.status_code == 200
    #assert response.data == b'Hello, World!'

@pytest.mark.parametrize("test_input,expected", [({"name":"rita","location":"NZ"},"done"),({"name":"seema"},"done")])
    
def test_upload(client,test_input, expected):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    
    data = test_input
    url = '/add'

    response = client.post(url, data=json.dumps(data), headers=headers)

    assert response.content_type == mimetype
    assert response.json['flag'] == data
    #assert response.status_code == 201
