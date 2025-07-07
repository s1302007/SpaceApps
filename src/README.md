# SpaceApps 2025 
This project simulates planetary geolocation, landmarks, and route data via a Flask-powered Web API. It's designed for the NASA Space Apps Challenge 2025.

## Remote Setup (VS Code)

### 1. Install VS Code Extensions
Install the following extensions in VS Code:
- [Remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)

### 2. Configure SSH in VS Code
1. Open the **Command Palette** (`Ctrl+Shift+P` or `Cmd+Shift+P`) and search for `Remote-SSH: Add New SSH Host...`
2. Enter your SSH connection string:
   ```bash
   ssh username@hostname

Replace username and hostname with your remote server details. Example:

ssh s1302007@163.143.90.121

### 3. Connect to Remote
1. Open **Command Palette** (`Ctrl+Shift+P` or `Cmd+Shift+P`) and select Remote-SSH: Connect to Host...
2. Choose your configured host (163.143.90.121) and Enter your password.
3. VS Code will open a new window connected to your remote server.

### 4. Open the project
Once connected, open the project folder:
```bash
$ cd /home/ot02/SpaceApps/src
```

### 5. Setup server
```bash
$ docker compose up --build
```

### 6. Open Web API
Visit http://163.143.90.121:5001/ in your local browser.

### 7. Git Pull and Push (Before and After Editing code)
Always pull latest changes before you start editing, and push changes after you are done, in case that there is a local setup user.

Pull the latest changes:
```bash
$ git pull origin main
```
After editing, add and commit your changes:
```bash
$ git add .
$ git commit -m "commit message"
```
Push your changes to repository:
```bash
$ git push origin main
```

## Local Setup (Git Control)

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
### 3. Set Up and Run MySQL (via Docker)
```bash
$ docker compose up --build
```

### 4. Open Web API 
Visit http://localhost:5001/ in local browser.

### 5. Git Pull and Push (Before and After Editing code)
Always pull latest changes before you start editing, and push changes after you are done.

Pull the latest changes:
```bash
$ git pull origin main
```
After editing, add and commit your changes:
```bash
$ git add .
$ git commit -m "commit message"
```
Push your changes to repository:
```bash
$ git push origin main
```