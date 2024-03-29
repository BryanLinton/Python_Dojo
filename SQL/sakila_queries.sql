-- SELECT city.city_id, city.city, customer.first_name, customer.last_name, customer.email, address.address FROM city 
-- JOIN address ON address.city_id = city.city_id
-- JOIN customer ON customer.address_id = address.address_id WHERE city.city_id = 312;

-- SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name FROM film
-- JOIN film_category ON film_category.film_id = film.film_id
-- JOIN category ON category.category_id = film_category.category_id WHERE category.name = "comedy";	

-- SELECT actor.actor_id, CONCAT(actor.first_name, " ", actor.last_name) AS actor_name, film.title, film.film_id, film.title, film.description FROM film
-- JOIN film_actor ON film_actor.film_id = film.film_id
-- JOIN actor ON actor.actor_id = film_actor.actor_id WHERE actor.actor_id = 5;

-- SELECT customer.store_id, city.city_id, customer.first_name, customer.last_name, customer.email, address.address
-- FROM customer
-- JOIN address ON customer.address_id = address.address_id
-- JOIN city ON address.city_id = city.city_id
-- WHERE customer.store_id = 1
-- AND city.city_id IN (1, 42, 312, 459);

-- SELECT film.title, film.description, film.release_year, film.rating, film.special_features 
-- FROM film
-- JOIN film_actor ON film.film_id = film_actor.film_id
-- JOIN actor ON actor.actor_id = film_actor.actor_id
-- WHERE film.rating = "G" AND film.special_features LIKE "%Behind the Scenes%" AND actor.actor_id = 15

-- SELECT film.film_id, film.title, actor.actor_id, CONCAT(actor.first_name, " ", actor.last_name) AS actor_name, actor.last_update
-- FROM film
-- JOIN film_actor ON film.film_id = film_actor.film_id
-- JOIN actor ON actor.actor_id = film_actor.actor_id
-- WHERE film.film_id = 369

-- SELECT film.film_id, film.title, film.description, film.release_year, film.rating, film.special_features, category.name, film.rental_rate  
-- FROM film
-- JOIN film_category ON film_category.film_id = film.film_id
-- JOIN category ON category.category_id = film_category.category_id 
-- WHERE category.name = "drama" AND film.rental_rate = 2.99

SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre, actor.first_name, actor.last_name
FROM actor
JOIN film_actor ON actor.actor_id = film_actor.actor_id
JOIN film ON film_actor.film_id = film.film_id
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE actor.first_name = 'Sandra' AND actor.last_name = 'Kilmer' AND category.name = 'Action';