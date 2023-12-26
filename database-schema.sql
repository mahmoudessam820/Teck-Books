-- PostgreSQL database 

CREATE TABLE IF NOT EXISTS "users" (
    "id" serial NOT NULL,
    "username" varchar(100) NOT NULL,
    "email" varchar(150) NOT NULL UNIQUE,
    "password" varchar(255) NOT NULL,
    PRIMARY KEY ("id")
)


CREATE TABLE IF NOT EXISTS "books" (
    "id" serial NOT NULL,
    "title" varchar(255) NOT NULL,
    "author" varchar(50) NOT NULL,
    "category" varchar(50) NOT NULL,
    "language" varchar(50) NOT NULL,
    "pages" int NOT NULL,
    "year" int NOT NULL,
    "link" varchar(255) NOT NULL,
    PRIMARY KEY ("id")
)