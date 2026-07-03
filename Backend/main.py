# For local test:
# Install Docker Engine (Linux) and run FastAPI backend against laptop's Docker daemon.
# Create test containers

# For phyton docker management: https://docker-py.readthedocs.io/en/stable/

from fastapi import FastAPI
import docker 

app = FastAPI()
client = docker.from_env()

def container_information(c):
    return {
        "id": c.id,
        "short_id": c.id[:12],
        "name": c.name.lstrip("/"),
        "logpath": c.attrs.get("LogPath"),
        "image": c.image.tags[0] if c.image.tags else None,
        "created": c.attrs.get("Created"),
        "state": c.attrs.get("State"),
        "ports": c.attrs.get("NetworkSettings", {}).get("Ports"),
    }

def container_summary(c):
    # print(c.attrs)
    # print(c)
    return {
        # First 12 characters
        "short_id": c.id[:12],
        # Remove leading character, '/'
        "name": c.name.lstrip("/"),
        "status": c.status,
        "image": c.image.tags[0] if c.image.tags else None,
        "created": c.attrs.get("Created"),
    }

@app.get("/")
def read_root():
    return {"Docker management backend using Docker SDK for Python."}

# Container endpoints
@app.get("/containers")
def list_containers():
    containers = client.containers.list(all=True)
    return [container_summary(c) for c in containers]

@app.get("/containers/{container_id}")
def list_container(container_id):
    c = client.containers.get(container_id)
    return container_information(c)

@app.post("/containers/{container_id}/start")
def start_container():
    return {}

@app.post("/containers/{container_id}/stop")
def stop_container():
    return {}

@app.delete("/containers/{container_id}")
def remove_container():
    return {}

@app.get("/containers/{container_id}/logs")
def read_container_logs():
    return {}




