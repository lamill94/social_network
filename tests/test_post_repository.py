from lib.post_repository import PostRepository
from lib.post import Post

# When we call all method
# We get a list of Post objects relflecting the seed data

def test_get_all_records(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)

    posts = repository.all()

    assert posts == [
        Post(1, 'The worst day', 'My car exploded!', 600, 1),
        Post(2, 'The best day', 'Hubby bought me a new car!', 700, 1),
        Post(3, 'Boring', 'Flew to Stanstead..yawn!', 100, 2),
        Post(4, 'Sunshine awaits me!', 'Flying to Hurghada today woo!', 200, 2),
        Post(5, 'Customers suck', 'Man customers are so dumb!', 20, 3),
        Post(6, 'Today was better', 'I was on with Adam so that makes things better', 50, 3)
    ]

# When we call create method
# We get a new record in the DB

def test_create_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    repository.create(Post(None, 'Test title', 'Test content', 100, 3))

    posts = repository.all()

    assert posts == [
        Post(1, 'The worst day', 'My car exploded!', 600, 1),
        Post(2, 'The best day', 'Hubby bought me a new car!', 700, 1),
        Post(3, 'Boring', 'Flew to Stanstead..yawn!', 100, 2),
        Post(4, 'Sunshine awaits me!', 'Flying to Hurghada today woo!', 200, 2),
        Post(5, 'Customers suck', 'Man customers are so dumb!', 20, 3),
        Post(6, 'Today was better', 'I was on with Adam so that makes things better', 50, 3),
        Post(7, 'Test title', 'Test content', 100, 3)
    ]