# Flask-JWT-API

Flask API using JWT token

## Flask User Api using JWT

## Usages

- Basic-authentication + x-access-token
- User can signup/create x-access-token and use todo api
- User have no access to User class
- Admin Can do `CRUD` operations on Users, Todo
- Password will saved as hased password
- User Can generate the X-access-token for get/post todo api

## Documentation

- Install all the dependencies

```bash
python -m pip install -r requirements.txt
```

- Add your secret key in `.env.example` and save as it `.env`.

- Load Environment variable

```bash
# linux
> export FLASK_APP=manage
> export FLASK_ENV=development
```

```cmd
# windows powershell
> $env:FLASK_APP=manage
> $env:FLASK_ENV=development
```

Get more details about the flask env check docs [here](https://flask.palletsprojects.com/en/1.1.x/cli/)

- Migrate the database

```bash
> flask db init
> flask db migrate -m "Initial migration."
> flask db upgrade
```

- Run the server

```bash
flask run
```

- Create a admin user on `url/user`. Give admin access using sql query
    <  Admin access need to perform admin level task such as deleting/upgrading user.

```json
{
    "username": "admin",
    "password": "admin",
}
```

- Get `x-access-token` on `url/login`

```json
{
    "username": "admin",
    "password": "admin",
}
```

- Perform All other operations using the jwt tokens.
- Todo Operations can done with x-access-token

## Example

```python
import requests

headers = {
"x-access-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFkbWluIn0.vrCzbqJLbP8wejP_ZE1hi2U3bSlRwF2rln02J0qmc9A"}

url = "http://127.0.0.1:5000/user"

json = { "todo_name": "Complete" }

#response = requests.get(url,headers=headers)
response = requests.post(url, json=json, headers=headers)
print(response.text)
```

## Upcoming Change in Repo

- Api limiter
- Blog API
