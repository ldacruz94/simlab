# SimLab

SimLab is a small Python service for running simulation jobs and retrieving 
their results through an API. 

The idea is to submit a simulation run with parameters, 
let it execute in the background, and then query its 
status and output later.

This project is a work in progress.

## Local Development - Getting Started

### Docker:

```bash
  docker build . -t simlab-api:latest
```

```bash
  docker run -e CREATE_TABLES=false -p 8000:8000 simlab-api
```

### FastAPI:

```bash
  fastapi dev
```