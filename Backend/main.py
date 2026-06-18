# For local test:
# Install Docker Engine (Linux) and run FastAPI backend against laptop's Docker daemon.
# Create test containers

# API endpoints
# GET    /containers
# GET    /containers/{id}
# POST   /containers/start/{id}
# POST   /containers/stop/{id}
# DELETE /containers/{id}
# GET    /containers/{id}/logs

# For phyton docker management: https://docker-py.readthedocs.io/en/stable/

# For laptop: https://docs.docker.com/engine/install/ubuntu/#installation-methods
from fastapi import FastAPI
import docker 

app = FastAPI()
client = docker.from_env()

@app.get("/")
def read_root():
    return {"Hello": "World"}

print(client.version())
# @app.get("/containers")
# def list_containser(all=False):
#     containers = client.containers.list(all=all)
#     return [
#         {"id": c.id[:12], "name": c.name, "status": c.status, "image": c.image.tags}
#         for c in containers
#     ]



