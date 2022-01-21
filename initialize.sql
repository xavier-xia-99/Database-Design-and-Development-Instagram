-- Setup the database for project

\c postgres;
DROP DATABASE IF EXISTS instagram;

CREATE database instagram;
\c instagram;

\i create.SQL;



-- First round of adding --
\copy "User" (user_id, display_name, password, bio)  FROM 'Users.csv' csv header

\copy Brands (brand_id, brand_name) FROM 'Brands.csv' csv header

\copy Ads (ad_id, brand_id) FROM 'Ads.csv' csv header

\copy Credit_cards(credit_card_num, CVV) FROM 'Credit_Cards.csv' csv header

\copy Post (post_id, user_id, date_posted, hashtag, location, description) FROM 'Posts.csv' csv header

\copy Accounts(acc_id, credit_card_num, date_bought, sub_tier) FROM 'Accounts.csv' csv header

\copy Subscriber_Accts (user_id, acc_id) FROM 'Subscriber_Accts.csv' csv header

\copy Free_user (user_id, date_joined) FROM 'Free_Users.csv' csv header

\copy Content_Creator (user_id, contact_email, business_cat) FROM 'Content_Creator.csv' csv header

\copy Follows (u1_user_id, u2_user_id) FROM 'Follows.csv' csv header
-- many to many --

\copy Views_Ad (user_id, ad_id, date_viewed) FROM 'Views_Ad.csv' csv header

\copy Views_Post (post_id, u2_user_id, date_viewed , u1_user_id) FROM 'Views_Post.csv' csv header

\copy Likes_Post (post_id, u2_user_id, date_liked, u1_user_id) FROM 'Likes_Post.csv' csv header

\copy Subscribes(u1_user_id, u2_user_id, donation_amt) FROM 'Subscribes.csv' csv header

-- ============================================================
  
