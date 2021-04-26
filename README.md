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

- install all the dependencies
- Create Db using the terminal

```bash
from main import db
db.create_all()
exit()
```

- run the server

```bash
python src/main.py
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

## Upcoming Change in Repo

- Api limiter
