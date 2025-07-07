# Planetary Web API – SpaceApps 2025 Project

This project simulates planetary geolocation, landmarks, and route data via a Flask-powered Web API. It's designed for the NASA Space Apps Challenge 2025.

## Getting Started (Local Development)

Ensure you have **Python 3**, **Docker**, and **Docker Compose** installed on your system.

### 1. Clone the Repository

```bash
$ git clone https://github.com/s1302007/SpaceApps.git
$ cd SpaceApps/src
```
### 2. Create and Activate Virtual Environment
```bash
# Linux/macOS
$ python3 -m venv .venv
$ source .venv/bin/activate
```
```bash
# Windows 
$ python -m venv .venv
$ .venv\Scripts\activate
```
4. Set Up and Run MySQL (via Docker)
```bash
$ docker compose up --build
```
5. Open http://localhost:5001/ in browser
