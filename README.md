# A movie rental service
A basic movie rental service with a built-in filebase database using Python, Django, and SQLite

## Create a Python development environment
- project uses Python 3.12 and above.
- install pipenv: `python3 -m pip install pipenv`
- use pipenv: -- `pipenv install` to install dependencies from the `./Pipfile`, you must be in the same directory as Pipfile.

## start project
- `python3 ./manage.py runserver` should be running on port:8882


## Features

- User authentication and registration
- Browse, search, and filter movies
- Rent and return movies
- Track rental history
- Admin interface for managing movies and users

## Project Structure

```
vidly/
├── manage.py
├── movies/
│   ├── models.py, views.py
│   └── ...
├── vidly/
│   ├── settings.py, urls.py
│   ├── ...
├── ...
└── Pipfile, Pipfile.lock, README.md,...
```

## Useful Commands

- Run migrations: `python3 ./manage.py migrate`
- Create superuser: `python3 ./manage.py createsuperuser`
- Run tests: `python3 ./manage.py test`

## License

This project is licensed under the MIT License.

