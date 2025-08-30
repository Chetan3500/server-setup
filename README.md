# DevOps Automation Portfolio

A project showcasing DevOps skills with Linux, Bash, Git, Docker, FastAPI, GitHub Actions, and Prometheus on AWS EC2.

## Phase 1: Automated Nginx Setup
- **Script**: `setup_server.sh`
- **Output**: `nginx_test.txt`, `screenshot.png`
- **Features**: Installs Nginx, creates webpage, logs setup.

## Phase 2: Containerized FastAPI Application
- **Files**: `main.py`, `Dockerfile`, `requirements.txt`, `docker_fastapi*.txt`, `fastapi_screenshot.png`
- **Features**: FastAPI app with /, /health, /info endpoints, containerized with Docker.

## Phase 3: CI/CD and Monitoring
Automates testing/deployment and monitors the FastAPI app.

### Prerequisites
- Ubuntu 22.04 (AWS EC2)
- Docker, Python 3, FastAPI, Uvicorn, Prometheus
- Ports 80, 8080, 8081, 8000, 9090 open in EC2 security group

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/Chetan3500/server-setup
   cd server-setup
   ```
2. Build and run FastAPI:
    ```bash
    docker build -t fastapi-app .
    docker build -d -p 8000:80 fastapi-app
    ```
3. Install Prometheus:
    ```bash
    sudo apt install prometheus -y
    sudo systemctl start prometheus
    ```
4. Configure Prometheus(`sudo nano /etc/prometheus/prometheus.yml`)
    ```yml
    - job_name: 'fastapi'
      static_configs:
      - targets: ['localhost:8000']
    ```
5. Access at

- FastAPI: `http://13.233.140.52:8000`
- Prometheus: `http://13.233.140.52:9090`

`13.233.140.52` -> public-ip

### CI/CD

- **Workflow**: `.github/workflows/ci.yml`.
- Tests `main.py` and build Docker image on push/pull request.

### Monitoringg

- Prometheus scrapes `/metrics` endpoint.
- Metrics: `http_requests_total`, `custom_requests_total`.

### FastAPI endpoints

- `get /` - welcome message
- `get /heatlth` - health check
- `get /info` - server info

### Files

- `main.py` - FastAPI app with logging
- `Dockerfile` - Docker configuration
- `requirements.txt` - Python dependencies
- `docker_fastapi*.txt` - Test outputs
- `fastapi_*.png` - Screenshot of API response
- `test_main.py`: Pytest tests
- `prometheus_ui.txt`, `prometheus_query.txt`, `custom_metrics.txt`, `custom_query.txt`: Monitoring outputs
- `prometheus_screenshot.png`: Prometheus UI
- `deploy_fastapi.txt`: Deployment output 

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

- Prometheus:

    ![](./prometheus_screenshot.png)

