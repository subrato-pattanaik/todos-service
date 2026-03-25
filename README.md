A backend server for todos API for learning purpose.

## Packages and framework

- uv as package manager
- Python 3.14
- FastAPI: go-to package for building APIs
- SQLModel: go-to package for building APIs with SQL database
- Hypercorn: go-to package for running FastAPI applications
- Pydantic models: go-to package for data validation

## Lets understand the architecture of this code

### MakeFile

- Just like we have npm script, we could use linux Makefile to run automated commands.
- It is used to run the application in different modes.
- It is also used to run the tests and format the code.
- It is also used to run the type checking.

### main.py

- It is the entry point of the application.
- It is responsible for creating the FastAPI instance and including the routers.
- It also includes the exception handlers for the application.
- It uses the lifespan context manager to initialize the database on startup and clean up resources on shutdown.

### database.py

- It is responsible for creating the database connection and initializing the database using SQLModel.
- SQLModel is ORM which is built on top of SQLAlchemy and Pydantic, simplifies the communication between the business logic and the database. Instead of writing SQL queries, we can use sql model methods and objects to interact with the database.
- In this file we define the engine which is the entry point to the database.
- We also define the init_db function which is responsible for creating the database tables.

### Exceptions

- We have a global exception handler in main.py which is responsible for handling the exceptions.
- Each service can define its own exceptions in the exceptions.py file. This exception class is then used by the service to raise exceptions.
- Service exceptions will inherit from the base exception class defined in the src/exceptions.py file.

## How to run this application

1. Clone the repo

```bash
git clone <repo-url>
```

2. Cd into the directory

```bash
cd todos-service
```

3. Install deps

```bash
uv sync
```

4. Run the application

```bash
make dev
```

## Database essentials

### Migrate a revision

1. Run the following command to create a migration version:

```bash
uv run alembic revision --autogenerate -m "<migration-message>"
```

2. Run the following command to apply the migration to the database:

```bash
uv run alembic upgrade head
```

### Undo a revision

To completely undo a revision, it's a two-step process:

1. Rollback the Database: First, you tell Alembic to revert the changes applied to your actual database tables by going down one revision:

```bash
uv run alembic downgrade -1
```

2. Delete the File: Then, you just delete the generated python migration file from the alembic/versions/ directory so Alembic forgets it ever existed.
