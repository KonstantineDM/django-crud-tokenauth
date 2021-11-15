# Django CRUD with Token authentication

An implementation of API created with Django REST framework.
The API offers the following services:
* register a User with provided username, email and password; provide a Token 
  for authentication of further User's requests;
* login a registered User with provided username, email, password ant Token;
* create an Account object with provided username and email, save it to database;
* read data of Account, stored in database or retrieve a list of all Accounts;
* update Account object stored in database;
* delete Account object stored in database.

## Dependencies
File `requirements.txt` lists all required libraries for the project. 

### Installation
Consecutively enter in your terminal:
```
python -m pip install Django
python -m pip install djangorestframework
python -m pip install python-dotenv
```
or just enter the following command
```
pip install -r requirements.txt
```

## API endpoints
Endpoint | HTTP Method | Operation
-- | -- |-- 
`api/authapp/register` | POST | Register User
`api/authapp/login` | POST | Login User
`api/crudapp/create` | POST | Create Account
`api/crudapp/<int:account_id>` | GET | Read single Account's data
`api/crudapp/accounts` | GET | Read list of Accounts
`api/crudapp/<int:account_id>/update` | PUT | Update Account data
`api/crudapp/<int:account_id>/delete` | DELETE | Update Account

## How to use
The API testing was conveyed through the service of [postman](https://www.postman.com/).

1. Run the django server. Enter in terminal (from inside the dir with manage.py):
```
python manage.py runserver
```
2. Start the postman agent.

3. Provide the request URL (e.g. `http://127.0.0.1:8000/api/authapp/register`).

4. Select request type (GET, POST, PUT, DELETE) and provide data for the 
   request's body (for `register` the data is: username, email, password, 
   password2).
   P.S. password and password2 must match (if they don't, appropriate error 
   is returned).
   ![1](https://user-images.githubusercontent.com/71542112/141827084-a65cd497-22bd-46ab-8ff5-1375b85cd17d.PNG)


5. Send the request. It will return the following answer:
```
{
    "status": "Registration successful.",
    "username": "testcase",
    "email": "testcase@gmail.com",
    "Authorization": "Token 1afd97872da2605cdbf889c4c2090d460eb3566b"
}
```
6. The `Authorization` key provides a Token for authentication.

7. For all  API operations (except `register`) a token must be provided in the 
   `Headers`, as a value for `Authorization` key. Token MUST be entered with 
   the word `Token` at the beginnig, separated by a space from the long streak 
   of numbers and letters.

8. Access other API operations as described in paragraph 4.

## Tests

Both apps (authapp, crudapp) are supplied with some tests of API's functionality.
To launch tests enter the following command in the terminal (while being inside 
the project's directory, where manage.py is):
```
python manage.py test
```
Provided are the following testcases:
1. Check if new User is registered properly.
2. Check if User can log in with their credentials and if response returns 
   an auth Token.
3. Check if new Account is created properly.
4. Check if Account data can be read.
5. Check if a list of all created accounts can be requested.
6. Check if created Account can be updated.
7. Check if Account is deleted properly.
