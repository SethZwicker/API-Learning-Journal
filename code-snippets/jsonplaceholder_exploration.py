import requests

def explore_jsonplaceholder():
    # GET all posts
    posts = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    
    # GET single post
    single_post = requests.get('https://jsonplaceholder.typicode.com/posts/1').json()
    
    # POST new post
    new_post = requests.post('https://jsonplaceholder.typicode.com/posts', 
                              json={
                                  'title': 'API Learning',
                                  'body': 'Exploring REST APIs',
                                  'userId': 1
                              }).json()
    
    return posts, single_post, new_post
