\connect postgres

drop database if exists instagram;
create database instagram;

\connect instagram;
-- You are now connected to database "instagram" as user "isdb".
\i create.SQL

\i initialize.SQL
\echo "The Users table shows all users and their sign-up information such as username, password, display_name, and bio. "
SELECT * FROM "User";

\echo "The Brands table shows every brand and its identifying brand_id."
SELECT * FROM Brands LIMIT 5;

\echo "The Ad table showsevery ad (by its unique id & the brand (by a brand_id) that created it."
SELECT * FROM Ads LIMIT 5;

\echo "The Credit_Cards table shows every user‘s credit card number and its CVV."
SELECT * FROM Credit_cards;

\echo "The Posts table shows every post, who created it and all information held within an Instagram post."
SELECT * FROM Post LIMIT 5;

\echo "The Accounts table shows all information related to user accounts."
SELECT * FROM Accounts LIMIT 10;

\echo "The Subscriber_Accts table shows all information related to Subscribers such as their user_id and personal acc_id."
SELECT * FROM Subscriber_Accts LIMIT 5;

\echo "The Free_User table represents all the free users currently on Instagram and when they started using it."
SELECT * FROM Free_user;

\echo "The Content Creators table shows all Content Creators and information about their work such as contact_email and business category."
SELECT * FROM Content_Creator;

\echo "The Follows table represents every user and which other users they follow."
SELECT * FROM Follows;

\echo "The Views_Ad table shows all the users who have seen an ad on any one date."
SELECT * FROM Views_Ad LIMIT 10;

\echo "The Views_Post table shows all the users when a user first saw a particular post."
SELECT * FROM Views_Post LIMIT 10;

\echo "The Likes_Post table shows all the users when a user liked a post."
SELECT * FROM Likes_Post LIMIT 10;

\echo "The Follows table represents every user and what Content Creators they are subscribed to."
SELECT * FROM Subscribes;
