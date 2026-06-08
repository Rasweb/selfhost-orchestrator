# selfhost-orchestrator
Monitor and control self-hosted apps on a Raspberry Pi.  

## Info
Build a browser-accessible app with a Python FastAPI backend and TypeScript React frontend, deployed on Raspberry Pi with Docker/Podman. 

A backend-first orchestration platform for self-hosted services:
- Manages and monitors 
- Exposes a cREST API
- Stores metadata, status history, and task schedules
- Serves a frontend UI for browser access

## Core features
**Backend API**
- service registry for apps
- health/status checks
- unified metadata endpoints
- auth for local admin access
- service launch URLs and control actions

**Service integration**
- adapter interface for each self-hosted app
- API responses with service status, version, url, uptime

**Local data layer**
- SQLite for config, tasks, status history
- simple ORM or data access layer

**Frontend client**
- React + Vite + TypeScript
- dashboard with cards for each service
- system metrics panel
- quick actions + links

**Deployment**
- Docker/Podman on Raspberry Pi
- optional Caddy reverse proxy
- network-accessible via browser
- connect with netbird

## Planned Stack
- Backend: Python + FastAPI
- Database: SQLite
- Frontend: Vue + TypeScript
- Deployment: Docker/Podman
- Auth: Session or token-based login


## Backend virtual environment
- Activate
``` bash
source .venv/bin/activate
```

- Check if active
``` bash
which python
```

- Upgrade pip
``` bash
python -m pip install --upgrade pip
```

- Install packages
``` bash
pip install "fastapi[standard]"
```

- Deactivate
``` bash
deactivate
```