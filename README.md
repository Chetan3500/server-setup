# DevOps Automation Portfolio

A project showcasing DevOps skills with Linux, Bash, Git, Docker, FastAPI, GitHub Actions, Prometheus, and Docker Compose on AWS EC2.

## Phase 1: Automated Nginx Setup
- **Script**: `setup_server.sh`
- **Output**: `nginx_test.txt`, `screenshot.png`
- **Features**: Installs Nginx, creates webpage, logs setup.

## Phase 2: Containerized FastAPI Application
- **Files**: `main.py`, `Dockerfile`, `requirements.txt`, `docker_fastapi*.txt`, `fastapi_screenshot.png`
- **Features**: FastAPI app with /, /health, /info endpoints, containerized.

## Phase 3: CI/CD and Monitoring
- **Files**: `test_main.py`, `ci.yml`, `prometheus_*.txt`, `custom_*.txt`, `prometheus_screenshot.png`
- **Features**: GitHub Actions CI/CD, Prometheus monitoring.

## Phase 4: Orchestration and Scaling
Production-like deployment with Docker Compose, Nginx load balancing, and Prometheus.

### Prerequisites
- Ubuntu 22.04 (AWS EC2)
- Docker, Docker Compose v2.29.1, Python 3, FastAPI, Nginx, Prometheus
- Ports 80, 8000-8002, 9090 open

### Setup Instructions
1. Clone:
   ```bash
   git clone https://github.com/Chetan3500/server-setup
   cd server-setup
   ```
2. Build and run FastAPI:
    ```bash
    docker compose up -d
    ```
3. Access at

- FastAPI: `http://13.233.140.52:80`
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
- `docker-compose.yml`, `nginx.conf`, `prometheus.yml`: Orchestration configs
- `project4_*.txt`: Deployment and monitoring outputs
- `nginx_screenshot.png`: Load balancer response

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

- Load Balancer:

    ![](./nginx_screenshot.png)

