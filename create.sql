-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2021-12-05 17:18:41.924

-- tables
-- Table: Accounts
-- DROP TABLE IF EXISTS Accounts;
-- DROP TABLE IF EXISTS Ads;
-- DROP TABLE IF EXISTS Brands;
-- DROP TABLE IF EXISTS Content_Creator;
-- DROP TABLE IF EXISTS Free_user;
-- DROP TABLE IF EXISTS "User";
-- DROP TABLE IF EXISTS Subscriber_Accts;
-- DROP TABLE IF EXISTS Credit_cards;


CREATE TABLE Accounts (
    acc_id int  NOT NULL,
    credit_card_num text  NOT NULL,
    date_bought date  NOT NULL,
    sub_tier text  NOT NULL,
    CONSTRAINT Accounts_pk PRIMARY KEY (acc_id)
);

-- Table: Ads
CREATE TABLE Ads (
    ad_id int  NOT NULL,
    brand_id int  NOT NULL,
    CONSTRAINT Ads_pk PRIMARY KEY (ad_id)
);

-- Table: Brands
CREATE TABLE Brands (
    brand_id int  NOT NULL,
    brand_name varchar  NOT NULL,
    CONSTRAINT Brands_pk PRIMARY KEY (brand_id)
);

-- Table: Content_Creator
CREATE TABLE Content_Creator (
    user_id int  NOT NULL,
    contact_email text  NOT NULL,
    business_cat text  NOT NULL,
    CONSTRAINT Content_Creator_pk PRIMARY KEY (user_id)
);

-- Table: Credit_cards
CREATE TABLE Credit_cards (
    credit_card_num text  NOT NULL,
    CVV int  NOT NULL,
    CONSTRAINT Credit_cards_pk PRIMARY KEY (credit_card_num)
);

-- Table: Follows
CREATE TABLE Follows (
    u1_user_id int  NOT NULL,
    u2_user_id int  NOT NULL,
    CONSTRAINT Follows_pk PRIMARY KEY (u1_user_id,u2_user_id)
);

-- Table: Free_user
CREATE TABLE Free_user (
    user_id int  NOT NULL,
    date_joined date  NOT NULL,
    CONSTRAINT Free_user_pk PRIMARY KEY (user_id)
);

-- Table: Likes_post
CREATE TABLE Likes_post (
    post_id int  NOT NULL,
    u2_user_id int  NOT NULL,
    date_liked date  NOT NULL,
    u1_user_id int  NOT NULL,
    CONSTRAINT Likes_post_pk PRIMARY KEY (post_id,u2_user_id,u1_user_id)
);

-- Table: Post
CREATE TABLE Post (
    post_id int  NOT NULL,
    user_id int  NOT NULL,
    date_posted date  NOT NULL,
    hashtag text  NOT NULL,
    location text  NOT NULL,
    description varchar(255)  NOT NULL,
    CONSTRAINT Post_pk PRIMARY KEY (post_id,user_id)
);

-- Table: Subscriber_Accts
CREATE TABLE Subscriber_Accts (
    user_id int  NOT NULL,
    acc_id int  NOT NULL,
    CONSTRAINT Subscriber_Accts_pk PRIMARY KEY (user_id)
);

-- Table: Subscribes
CREATE TABLE Subscribes (
    u1_user_id int  NOT NULL,
    u2_user_id int  NOT NULL,
    donation_amt int  NOT NULL,
    CONSTRAINT Subscribes_pk PRIMARY KEY (u1_user_id,u2_user_id)
);

-- Table: User
CREATE TABLE "User" (
    user_id int  NOT NULL,
    display_name text  NOT NULL,
    password text  NOT NULL,
    bio text  NOT NULL,
    CONSTRAINT User_pk PRIMARY KEY (user_id)
);

-- Table: Views_ad
CREATE TABLE Views_ad (
    user_id int  NOT NULL,
    ad_id int  NOT NULL,
    date_viewed date  NOT NULL,
    CONSTRAINT Views_ad_pk PRIMARY KEY (user_id,ad_id,date_viewed)
);

-- Table: Views_post
CREATE TABLE Views_post (
    post_id int  NOT NULL,
    u2_user_id int  NOT NULL,
    date_viewed date  NOT NULL,
    u1_user_id int  NOT NULL,
    CONSTRAINT Views_post_pk PRIMARY KEY (post_id,u2_user_id,date_viewed,u1_user_id)
);

-- foreign keys
-- Reference: Ads_Brands (table: Ads)
ALTER TABLE Ads ADD CONSTRAINT Ads_Brands
    FOREIGN KEY (brand_id)
    REFERENCES Brands (brand_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Likes_post_Post (table: Likes_post)
-- ALTER TABLE Likes_post ADD CONSTRAINT Likes_post_Post
--     FOREIGN KEY (post_id)
--     REFERENCES Post (post_id)  
--     NOT DEFERRABLE 
--     INITIALLY IMMEDIATE
-- ;

-- Reference: Likes_post_User (table: Likes_post)
ALTER TABLE Likes_post ADD CONSTRAINT Likes_post_User
    FOREIGN KEY (u2_user_id)
    REFERENCES "User" (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Post_User (table: Post)
ALTER TABLE Post ADD CONSTRAINT Post_User
    FOREIGN KEY (user_id)
    REFERENCES "User" (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Subscribes_Content_Creator (table: Subscribes)
ALTER TABLE Subscribes ADD CONSTRAINT Subscribes_Content_Creator
    FOREIGN KEY (u2_user_id)
    REFERENCES Content_Creator (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Subscribes_Subscriber (table: Subscribes)
ALTER TABLE Subscribes ADD CONSTRAINT Subscribes_Subscriber
    FOREIGN KEY (u1_user_id)
    REFERENCES Subscriber_Accts (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Views_ad_Ads (table: Views_ad)
ALTER TABLE Views_ad ADD CONSTRAINT Views_ad_Ads
    FOREIGN KEY (ad_id)
    REFERENCES Ads (ad_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Views_ad_User (table: Views_ad)
ALTER TABLE Views_ad ADD CONSTRAINT Views_ad_User
    FOREIGN KEY (user_id)
    REFERENCES "User" (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Views_post_Post (table: Views_post)
-- ALTER TABLE Views_post ADD CONSTRAINT Views_post_Post
--     FOREIGN KEY (post_id)
--     REFERENCES Post (post_id)  
--     NOT DEFERRABLE 
--     INITIALLY IMMEDIATE
-- ;

-- Reference: Views_post_User (table: Views_post)
ALTER TABLE Views_post ADD CONSTRAINT Views_post_User
    FOREIGN KEY (u2_user_id)
    REFERENCES "User" (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: account_ccard (table: Accounts)
ALTER TABLE Accounts ADD CONSTRAINT account_ccard
    FOREIGN KEY (credit_card_num)
    REFERENCES Credit_cards (credit_card_num)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: accounts (table: Subscriber_Accts)
ALTER TABLE Subscriber_Accts ADD CONSTRAINT accounts
    FOREIGN KEY (acc_id)
    REFERENCES Accounts (acc_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: follow (table: Follows)
-- ALTER TABLE Follows ADD CONSTRAINT follower
--     FOREIGN KEY (u1_user_id1)
--     REFERENCES "User" (user_id)  
--     NOT DEFERRABLE 
--     INITIALLY IMMEDIATE
-- ;

-- -- Reference: followed_by_id1 (table: Follows)
-- ALTER TABLE Follows ADD CONSTRAINT followed_by_id1
--     FOREIGN KEY (u2_user_id2)
--     REFERENCES "User" (user_id)  
--     NOT DEFERRABLE 
--     INITIALLY IMMEDIATE
-- ;

-- Reference: liked_by (table: Likes_post)
ALTER TABLE Likes_post ADD CONSTRAINT liked_by
    FOREIGN KEY (u1_user_id)
    REFERENCES "User" (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: viewed_by (table: Views_post)
ALTER TABLE Views_post ADD CONSTRAINT viewed_by
    FOREIGN KEY (u1_user_id)
    REFERENCES "User" (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

