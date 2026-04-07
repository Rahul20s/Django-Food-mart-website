# Django Food Mart Website

A full-featured food ordering and management platform built with Django.

## Features

- User registration and authentication
- Restaurant owner dashboard
- Customer food browsing and ordering
- Admin panel for management
- Profile management with user types (Customer, Restaurant, Admin)

## Tech Stack

- **Backend**: Django 6.0
- **Database**: SQLite (development)
- **Frontend**: HTML, CSS, Bootstrap
- **Authentication**: Django's built-in auth system

## Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/Rahul20s/Django-Food-mart-website.git
   cd Django-Food-mart-website
   ```

2. Install dependencies:
   ```bash
   pip install django django-extensions pillow
   ```

3. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Start the development server:
   ```bash
   python manage.py runserver
   ```

5. Visit `http://127.0.0.1:8000/` in your browser.

## Deployment

This Django application requires a Python-capable hosting platform. Recommended options:

- [Render](https://render.com/)
- [Railway](https://railway.app/)
- [Fly.io](https://fly.io/)
- [Heroku](https://heroku.com/)

## Project Structure

```
food/           # Main app for food items and views
users/          # User authentication and profiles
mysite/         # Django project settings
static/         # Static files (CSS, images)
templates/      # HTML templates
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).