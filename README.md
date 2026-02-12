# Sample Backend API – Pytest + CI

This project demonstrates a sample Django backend API with automated testing using Pytest and continuous integration via GitHub Actions.

The goal is to establish a clean testing foundation from the beginning to prevent technical debt and regressions as the backend grows.

---

## 🚀 Features

- Create booking endpoint
- Fetch bookings endpoint
- Availability check endpoint
- Automated testing with pytest
- CI pipeline using GitHub Actions
- Clean repository structure with `.gitignore`

---

##  API Endpoints

### 1️⃣Create Booking
`POST /api/bookings/`

Request Body:

```json
{
  "user_id": 1,
  "flight_id": 10,
  "seats": 2
}


{
  "id": 1,
  "user_id": 1,
  "flight_id": 10,
  "seats": 2
}
```

### 2️⃣Fetch Bookings
GET /api/bookings/

Returns a list of bookings.

### 3️⃣Availability Check
GET /api/availability/?flight_id=10&travel_date=2026-02-12&seats=2

```
{
  "available": true,
  "remaining_seats": 48
}
```

### Tech Stack
- Python 3.13
- Django 6
- Django REST Framework
- Pytest
- Pytest-Django
- GitHub Actions

### Local Setup
1️⃣ Clone the repository
git clone https://github.com/dua-devs/Sample-Backend-API-Set-Up-Automated-Tests-Pytest-.git
cd Sample-Backend-API-Set-Up-Automated-Tests-Pytest-

2️⃣ Create virtual environment
python -m venv .venv
.venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run migrations
python manage.py migrate

5️⃣ Run server
python manage.py runserver

### Running Tests
Run all tests with a single command:
pytest

## ✅Covered Scenarios
- Successful booking creation
- Fetching bookings list
- Availability validation
- Missing parameters (edge cases)

### 🔄Continuous Integration
-This project includes a GitHub Actions workflow:
-Runs on push & pull requests
-Installs dependencies
-Executes pytest
-Fails automatically if tests fail
-CI ensures backend stability and prevents regressions.

### Test Structure
-Tests located inside bookings/
-Uses pytest + pytest-django
-Focused on critical flows
-Designed to scale as the backend grows


###👩‍💻 Author
Dua Salim Al Aufi
Backend Engineering – Sample API + Automated Testing
