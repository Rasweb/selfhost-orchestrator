# Selfhost Orchestrator
A lightweight orchestration platform for homelab
and self-hosted services.

## Features
- Service monitoring
- Health checks
- Docker integration
- Historical metrics
- Scheduled jobs
- Notifications
- Multi-host architecture
- Raspberry Pi optimized

## Built with
- FastAPI
- Vue
- TypeScript
- SQLite
- Docker
---

# Planning INFO
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

## Layers 
+---------------+
| Frontend      |
+---------------+
        |
+---------------+
| FastAPI API   |
+---------------+
        |
+---------------+
| Adapter Layer |
+---------------+
        |
+---------------+
| Services      |
| Service1      |
| Service2      |
| Service3      |
| RSS           |
| Future apps   |
+---------------+

## Features that may be implemented
Version 1

### Dashboard
Cards:
+----------------------+
| Service1             |
| Online               |
| Uptime: 4d 12h       |
| Version: 0.9.4       |
| [Open] [Restart]     |
+----------------------+

+----------------------+
| Service2             |
| Online               |
| Response: 45ms       |
| [Open] [Restart]     |
+----------------------+

### Service Registry
- id
- name
- url
- healthcheck_url
- adapter_type
- icon
- description

### Health Monitoring
Background tasks:
- Ping services
- Save results

Store history:
- service_id
- status
- response_time
- timestamp

### Metrics
- CPU
- RAM
- Disk
- Temperature

### Docker Container Management
- Running containers
- Stopped containers
- Restart container
- View logs

### Scheduled Tasks:
- Restart Service
- Backup Service
- Cleanup logs

### Notification System
- Service down
- Disk > 90%
- CPU > 80%

### Backup Manager
- Backup Service
- Store backups on different places

### Audit Logs:
- User logged in
- Service restarted
- Backup created

### Home dashboard 
- Today's feed(RSS)
- Recent saved articles
- Service health
- System status
- Recent backups
