# Planetary Web API – SpaceApps 2025 Project

This project simulates planetary geolocation, landmarks, and route data via a Flask-powered Web API. It's designed for the NASA Space Apps Challenge 2025.

## Getting Started (Local Development)

Ensure you have **Python 3**, **Docker**, and **Docker Compose** installed on your system.

### 1. Clone the Repository

```bash
$ git clone https://github.com/<your-org-or-username>/<repo-name>.git
$ cd <repo-name>/src
```
### 2. Create and Activate Virtual Environment
```bash
# Linux/macOS
$ python3 -m venv .venv
$ source .venv/bin/activate
```
```bash
# Windows (CMD)
$ python -m venv .venv
$ .venv\Scripts\activate.bat
```
4. Set Up and Run MySQL (via Docker)
```bash
$ docker compose up --build
```
