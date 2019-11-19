## Bookworm

Purpose


* A user should be able to create an account for himself on the website and set a password
* The user can see a list of books that exist in the system, and can also add books himself
* Books have the usual fields: title, author, year of publishing, and an optional short summary
* User can write a review for any book; a review consists of a numeric score between 0 and 5, and some text
* For each Book an average review score is generated and visible to all users
* The app can list all books, sorted by their average review score
* The app can list all the books written by a specific author


## Requirements

* Django >= v2.2
* Python >= v3.5
* Pytest
* sqlite