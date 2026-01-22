
# SKILEMAN BACKEND LOGIN TASK BUILT ON MODERN FASTAPI AND SQLMODEL

A high-performance, stateless authentication API built with **FastAPI** and **SQLModel**.

## 🚀 Key Professional Features

-   **Modern Lifespan Management**: Uses the latest FastAPI `lifespan` context manager for database initialization and seeding, Auto create user on startu (replacing deprecated startup events).
-   **SQLModel & SQLite**: Leverages SQLModel to unify Pydantic schemas and SQLAlchemy models into a single, type-safe source of truth.
-   **Advanced Security**:
    -   **Argon2 Hashing**: Uses `pwdlib[argon2]` for password encryption (Algorithm Provides high level security over counterpats such as python-jose and bycrypt).
    -   **Stateless JWT**: Implements `pyjwt` for secure, scalable authentication tokens.
-   **Layered Architecture**: Decouples business logic from API routes using a **Service Layer** pattern and **Dependency Injection**.
-   **Type-Safe Configuration**: Managed via `pydantic-settings` to ensure environment variables are validated at runtime.

---

## 🛠️ Setup & Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd skileMan

2. **Create a virtual environment**
    Run the cmd:
        python -m venv venv

    Activate your virtual env to manage dependencies
        Run the cmd:
            venv\Scripts\activate.bat     on windows

3. **Install dependencies**
    Run the cmd:
        pip install -r requirements.txt

4. **Configure Environment**
    Create a .env file in the root directory or
    if on windows simply Run the cmd: 
        echo > .env

    Replace the content of .env file with the conde snippet below:
        SECRET_KEY="your_super_secret_key_here"
        DATABASE_URL=sqlite:///./sql_app.db
        ACCESS_TOKEN_EXPIRE_MINUTES=60

## Run the Application:
    Bash

    fastapi dev app/main.py
    🧪 Testing the API
    Interactive Docs: Once the server is running, visit http://127.0.0.1:8000/docs.

## NB:
Create User: The application automatically Creates a test user on first run, thanks to fastApI `Lifespan`

## user Login Credentials ##
    Email: admin@gmail.com
    Password: password123

## To add more users: 
 -   Navigate to skileMan/main.py 
 -   change the email and password
 -   quit and restart the server

## Authentication:

- Use the /login endpoint to receive a JWT.

- Use the token for authorized requests in the Authorization: Bearer <token> header.


---

### 🔍 Project Structure 

1.  **`app/main.py`**: Entry point with `lifespan`.
2.  **`app/core/`**: `config.py` (settings), `loggins`(info to console) and `security.py` (Argon2/JWT).
3.  **`app/db/`**: `session.py` (engine/SessionDep) and `models/` (User table).
4.  **`app/api/v1/`**: `auth.py` (routes).
5.  **`app/services/`**: `auth_service.py` (logic).
6.  **`requirements.txt`**: All libraries listed earlier.
7. **`venv/...`** :            virtual enviroment
7. **`.env`**   :              enviromental variables such as Secret keys
7. **`.gitignore`** :          secret paths e.g .env etc
7. **`requirements.txt`**  :   dependencies
7. **`README.md`**    :        documentation
7. **`skile_man.db`**  :       databse storage

## Project Structure Detailed view

```
skileMan/
├── app/
│   ├── api/
│   │   └── v1/
│   │       └── api.py           # Route handler
│   │       
│   ├── core/
│   │   ├── config.py            # App settings
|   |   ├── logging.py           # logs info to console
│   │   └── security.py          # Password hashing & JWT
│   ├── db/
│   │   ├── session.py           # Engine & Session setup
│   │   └── models/
│   │       └── user.py          # SQLModel definition
│   ├── services/
│   │   └── auth_service.py      # Business logic
│   └── main.py                  # Entry point
├── venv/...                     # virtual enviroment
├── .env                         # enviromental variables such as Secret keys
├── .gitignore
├── requirements.txt            #dependencies
├── README.md                   #documentation
└── skile_man.db                #databse storage

```