# credicxo_assignment

## Build
```
$ git clone https://github.com/avashishta5/credicxo_assignment.git
$ cd credicxo_assignment
$ virtualenv venv
$ pip3 install -r requirements.txt
$ cd credicxo_test
```
In `credicxo_test/settings.py`, update the following values: 
```
31 DBNAME = <database_name>
32 DBUSER = <database_user>
33 DBPASS = <database_password>
```
Then,
```
$ python3 manage.py migrate
(optionally) $ python3 manage.py createsuperuser
$ python3 manage.py runserver
```

## Routes
In the browseable api,
1. Register new user (POST)
`localhost:8000/rest-auth/registration/`
2. Login (POST)
`localhost:8000/rest-auth/login/`
3. Logout (POST)
`localhost:8000/rest-auth/logout/`
4. Forgot Password/Rest Password (POST)
`localhost:8000/rest-auth/password/change/`
5. Current User (GET)
`localhost:8000/rest-auth/user/`

The above methods use JWT for authentication, however to issue, refresh and verify JWT,
1. Get New Token (POST)
`localhost:8000/api-token-auth/`
2. Refresh Token (POST)
`localhost:8000/api-token-refresh/`
3. Verify Token (POST)
`localhost:8000/api-token-verify/`

To view data,
1. Teachers (GET/POST/UPDATE/DELETE)
`localhost:8000/teachers/`
2. Students (GET/POST/UPDATE/DELETE)
`localhost:8000/students/`

The views are implemented using viewsets and thus all routes for all verbs are auto-generated, and can be accessed using the browseable API. To delete or update individual entries, simply visit the link of the entry `localhost:8000/<teachers or students>/<id>`. The can alse be obtained by making a GET request to the main `/teachers/` or `/students/` endpoints as the serializer extends a `HyperlinkedModelSerializer`. 

### Adding users to groups
```
$ python3 manage.py shell
>> from django.contrib.auth.models import Group
>> group = Group.objects.get(name='<Teacher/Student/Admin>')
>> group.user_set.add(<username>)
```

## TODO
- Groups have not been implemented programmatically, only via the Admin Panel.
- CustomUser model needs to be modified to reflect the 3 classes of users based on groups.
