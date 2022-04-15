# DRF_Blog_API
An API for simple blog built with Django, Django Rest Framework and Postgres database. 

Clone project:<br>
git clone git@github.com:daelynum/DRF_Blog_API.git<br>

Install requirements:<br>
pip3 install -r requirements.txt <br>

Routes:<br>

POST a post <br>
127.0.0.1:8000/api/posts/<br>

request: <br>
```json
{
    "post": {
        "header": "Post 3",
        "content": "Text...",
        "author": "User5"
    }
}
```

GET posts <br>
127.0.0.1:8000/api/posts/<br>

response:
```json
{
    "posts": [
        {
            "id": 1,
            "author": "vladimir",
            "header": "text number 1",
            "content": "first text"
        },
        {
            "id": 2,
            "author": "",
            "header": "",
            "content": ""
        }
    ]
}
```

GET one post <br>
127.0.0.1:8000/api/post/{id}/<br>

response: <br>
```json
{
    "post": {
        "id": 1,
        "author": "vladimir",
        "header": "text number 1",
        "content": "first text"
    }
}
```

POST comment <br>
127.0.0.1:8000/api/post/{id}/comments/ <br>
request: <br>

parent == null when post is commented. Specify a parent_id when commenting a comment <br>
```json
{
    "parent": null,
    "author": "vladimir",
    "content": "Some text"
}
```

GET all comments for one post <br>
127.0.0.1:8000/api/post/{id}/comments/ <br>
response: <br>

```json
{
    "comments": [
        {
            "id": 1,
            "post": 1,
            "author": "first user",
            "content": "Some text",
            "parent": null,
            "reply": []
        },
        {
            "id": 2,
            "post": 1,
            "author": "second user",
            "content": "Some text",
            "parent": null,
            "reply": []
        },
        {
            "id": 3,
            "post": 1,
            "author": "third user",
            "content": "Some text",
            "parent": null,
            "reply": [
                {
                    "id": 7,
                    "post": 1,
                    "author": "first user",
                    "content": "Some text",
                    "parent": 3,
                    "reply": [
                        {
                            "id": 8,
                            "post": 1,
                            "author": "third user",
                            "content": "Some text",
                            "parent": 7,
                            "reply": null
                        }
                    ]
                }
            ]
        }
    ]
}
```

GET all comments for one post with nesting level parameter <br>
127.0.0.1:8000/api/post/{id}/comments/?nesting-level=2 <br>
response: <br>

```json
{
    "comments": [
        {
            "id": 1,
            "post": 1,
            "author": "first user",
            "content": "Some text",
            "parent": null,
            "reply": []
        },
        {
            "id": 2,
            "post": 1,
            "author": "second user",
            "content": "Some text",
            "parent": null,
            "reply": []
        },
        {
            "id": 3,
            "post": 1,
            "author": "third user",
            "content": "Some text",
            "parent": null,
            "reply": [
                {
                    "id": 7,
                    "post": 1,
                    "author": "first user",
                    "content": "Some text",
                    "parent": 3,
                    "reply": null
                }
            ]
        }
    ]
}
```

GET comments <br>
127.0.0.1:8000/api/post/{id}/comment/{id}/ <br>

```json
{
    "comment": [
        {
            "id": 3,
            "post": 1,
            "author": "first user",
                    "content": "Some text",
            "parent": null,
            "reply": [
                {
                    "id": 7,
                    "post": 1,
                    "author": "second user",
                    "content": "Some text",
                    "parent": 3,
                    "reply": [
                        {
                            "id": 8,
                            "post": 1,
                            "author": "third user",
                            "content": "Some text",
                            "parent": 7,
                            "reply": null
                        }
                    ]
                },
                {
                    "id": 11,
                    "post": 1,
                    "author": "third user",
                    "content": "Some text",
                    "parent": 3,
                    "reply": []
                }
            ]
        }
    ]
}
```

GET comments <br>
127.0.0.1:8000/api/post/{id}/comment/{id}/?nesting-level=2 <br>

```json
{
    "comment": [
        {
            "id": 3,
            "post": 1,
            "author": "first user",
            "content": "Some text",
            "parent": null,
            "reply": [
                {
                    "id": 7,
                    "post": 1,
                    "author": "second user",
                    "content": "Some text",
                    "parent": 3,
                    "reply": null
                },
                {
                    "id": 11,
                    "post": 1,
                    "author": "third user",
                    "content": "Some text",
                    "parent": 3,
                    "reply": null
                }
            ]
        }
    ]
}
```
