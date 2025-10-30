-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS accounts;
DROP SEQUENCE IF EXISTS accounts_id_seq;
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS accounts_id_seq;
CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    email text,
    username text
);

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title text,
    content text,
    views int,
    account_id int,
    constraint fk_account foreign key(account_id)
    references accounts(id)
    on delete cascade
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO accounts (email, username) VALUES ('laurenm@gmail.com', 'lamill94'); 
INSERT INTO accounts (email, username) VALUES ('claudiom@gmail.com', 'claudioAudio'); 
INSERT INTO accounts (email, username) VALUES ('stinkylara@gmail.com', 'IStinkNice');

INSERT INTO posts (title, content, views, account_id) VALUES ('The worst day', 'My car exploded!', 600, 1);
INSERT INTO posts (title, content, views, account_id) VALUES ('The best day', 'Hubby bought me a new car!', 700, 1);
INSERT INTO posts (title, content, views, account_id) VALUES ('Boring', 'Flew to Stanstead..yawn!', 100, 2);
INSERT INTO posts (title, content, views, account_id) VALUES ('Sunshine awaits me!', 'Flying to Hurghada today woo!', 200, 2);
INSERT INTO posts (title, content, views, account_id) VALUES ('Customers suck', 'Man customers are so dumb!', 20, 3);
INSERT INTO posts (title, content, views, account_id) VALUES ('Today was better', 'I was on with Adam so that makes things better', 50, 3);
