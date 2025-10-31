from lib.post import Post

# Test constructor

def test_constructor():
    post = Post(1, 'The worst day', 'My car exploded!', 600, 1)
    assert post.id == 1
    assert post.title == 'The worst day'
    assert post.content == 'My car exploded!'
    assert post.views == 600
    assert post.account_id == 1

# Test that two posts are equal to each other

def test_posts_are_equal():
    post1 = Post(1, 'The worst day', 'My car exploded!', 600, 1)
    post2 = Post(1, 'The worst day', 'My car exploded!', 600, 1)
    assert post1 == post2

# Test that post formats nicely

def test_post_formats_nicely():
    post = Post(1, 'The worst day', 'My car exploded!', 600, 1)
    assert str(post) == "Post(1, The worst day, My car exploded!, 600, 1)"