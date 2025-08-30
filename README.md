# DevOps Automation Portfolio

A project demonstrating DevOps skills with Linux, Bash, Git, Docker, and FastAPI on AWS EC2.

## Phase 1: Automated Nginx Setup
- **Script**: `setup_server.sh`
  - Automates Nginx installation and webpage setup.
- **Output**: `nginx_test.txt` (curl output), `screenshot.png` (webpage).
- **Features**:
  - Updates system packages.
  - Installs and starts Nginx.
  - Creates a webpage at `/var/www/html/index.html`.
  - Logs to `/var/log/setup_server.log`.

## Phase 2: Containerized FastAPI Application
A FastAPI app containerized with Docker, deployed on AWS EC2.

### Prerequisites
- Ubuntu 22.04 (AWS EC2)
- Docker, Python 3, FastAPI, Uvicorn
- Ports 80, 8080, 8081, 8000 open in EC2 security group

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/Chetan3500/server-setup
   cd server-setup
   ```
2. Build Docker image:
    ```bash
    docker build -t fastapi-app .
    ```
3. Run container:
    ```bash
    docker build -d -p 8000:80 fastapi-app
    ```
4. Access at `http://13.233.140.52:8000`

### endpoints

- `get /` - welcome message
- `get /heatlth` - health check
- `get /info` - server info

### files

- `main.py` - FastAPI app with logging
- `Dockerfile` - Docker configuration
- `requirements.txt` - Python dependencies
- `docker_fastapi*.txt` - Test outputs
- `fastapi_*.png` - Screenshot of API response

### Screenshots

- Nginx:
    ![](./Screenshot_2025-08-27_14-27-09.png)
- FastAPI:
    
    - `GET /`
    ![](./fastapi_root.png)
    - `GET /health`
    ![](./fastapi_health.png)
    - `GET /INFO
    ![](./fastapi_info.png)

