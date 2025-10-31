from lib.post import Post

class PostRepository:

    # Initialise with DB connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all posts
    def all(self):
        rows = self._connection.execute_query('SELECT * from posts')
        posts = []
        for row in rows:
            item = Post(row["id"], row["title"], row["content"], row["views"], row["account_id"])
            posts.append(item)
        return posts
    
    # Create a new post
    def create(self, post):
        rows = self._connection.execute_query('INSERT INTO posts (title, content, views, account_id) VALUES (%s, %s, %s, %s) RETURNING id', [post.title, post.content, post.views, post.account_id])
        row = rows[0]
        return row["id"]