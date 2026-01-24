
# High-Level Architecture

This is the design that I'm considering as a first iteration.

A client will send an authenticated call to
the API which will validate the request
and create a job ID and store it in a postgreSQL.

Afterwards, the API will enqueue the task to RabbitMQ
and the celery worker will execute the task.

Finally, the Celery worker will send an update back to the API
to update the job status.

The client will be able to call the API to check the status on the task executed.

```
┌──────────────┐
│   Client     │
│ (CLI / UI)   │
└──────┬───────┘
       │ HTTP (JSON)
       ▼
┌────────────────────┐
│      FastAPI       │   ← Control Plane
│  (API Gateway)     │
│────────────────────│
│ - Validate request │
│ - Create job ID    │
│ - Persist metadata │
│ - Enqueue task     │
└──────┬─────────────┘
       │ Celery Task (AMQP)
       ▼
┌────────────────────┐
│     RabbitMQ       │
│────────────────────│
│ Queue:             │
│ - simulation.jobs  │
│ - (DLQ optional)   │
└──────┬─────────────┘
       │
       │ Pull task
       ▼
┌────────────────────┐
│   Celery Worker    │   ← Execution Plane
│────────────────────│
│ - Deserialize job  │
│ - Load simulation  │
│ - Execute          │
│ - Track progress   │
│ - Handle retries   │
└──────┬─────────────┘
       │
       │ Results / Status
       ▼
┌────────────────────┐
│  Persistence Layer │
│────────────────────│
│ Postgres:          │
│ - job metadata     │
│ - state transitions│
│ - errors           │
│                    │
│ Object Storage:    │
│ - large outputs    │
└─────────┬──────────┘
          │
          │ HTTP Polling / Webhook
          ▼
┌────────────────────┐
│      Client        │
│ - Check status     │
│ - Fetch results    │
└────────────────────┘
```