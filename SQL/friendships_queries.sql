-- SELECT users.first_name, users.last_name, user2.first_name as friend_first_name, user2.last_name as friend_last_name
-- FROM users 
-- JOIN friendships ON friendships.user_id = users.id
-- JOIN users as user2 ON friendships.friend_id = user2.id WHERE user2.first_name = "Kermit"

-- SELECT COUNT(user_id) as total_friendships 
-- FROM users 
-- JOIN friendships ON friendships.user_id = users.id
-- JOIN users as user2 ON friendships.friend_id = user2.id 

-- SELECT user_id, CONCAT(users.first_name, " ", users.last_name) as User, COUNT(user_id) as total_friendships 
-- FROM users 
-- JOIN friendships ON friendships.user_id = users.id
-- JOIN users as user2 ON friendships.friend_id = user2.id 
-- GROUP BY user_id ORDER BY total_friendships DESC

-- INSERT INTO users (first_name, last_name, created_at, updated_at)
-- VALUES("Bubba", "Gump", NOW(), NOW())
-- INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
-- VALUES(6, 2, now(), now()) 
-- INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
-- VALUES(6, 4, now(), now())
-- INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
-- VALUES(6, 5, now(), now())

-- select friend_id, first_name, last_name 
-- from friendships 
-- LEFT JOIN users ON friendships.user_id = users.id where friend_id = 2 ORDER BY last_name ASC

-- DELETE FROM friendships WHERE user_id = 2 AND friend_id = 5

-- SELECT users.first_name, users.last_name, user2.first_name as friend_first_name, user2.last_name as friend_last_name
-- FROM users 
-- JOIN friendships ON friendships.user_id = users.id
-- JOIN users as user2 ON friendships.friend_id = user2.id 

