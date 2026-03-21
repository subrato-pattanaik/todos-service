# Lets understand the architecture of this code

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
