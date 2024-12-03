# test_views.py
'''module for testing the index view of my project'''

def test_index(client):
    '''tests the index page of my project'''
    #makes a get request, then stores the response code
    response = client.get('/')
    #checks to see if the status code is 200 (OK)
    assert response.status_code == 200
