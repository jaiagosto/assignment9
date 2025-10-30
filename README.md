# 🧮 Assignment 9 - FastAPI Calculator with PostgreSQL

**Author:** Jailene Agosto  
**GitHub:** [jaiagosto](https://github.com/jaiagosto)  
**Docker Hub:** [jaiagosto](https://hub.docker.com/u/jaiagosto)

---

## 📋 Project Overview

This project extends the FastAPI Calculator from Assignment 8 by integrating a PostgreSQL database and pgAdmin for database management. You can perform arithmetic operations through the web interface while learning SQL database operations.

**Key Components:**
- ✅ FastAPI Calculator Web Application
- ✅ PostgreSQL Database
- ✅ pgAdmin Web Interface
- ✅ Docker Compose Setup

---

## 🎯 Features

- **Calculator Operations:** Add, subtract, multiply, divide
- **PostgreSQL Database:** Store users and calculations
- **pgAdmin Interface:** Manage database through web UI
- **Docker Setup:** All services containerized
- **SQL Practice:** Create, insert, query, update, delete operations

---

## 🛠️ Technologies Used

- **FastAPI** - Web framework
- **PostgreSQL** - Database
- **pgAdmin** - Database management tool
- **Docker & Docker Compose** - Containerization
- **Python 3.10** - Programming language

---

## 🚀 Getting Started

### Prerequisites

- Docker Desktop installed and running
- Git installed

### 1. Clone the Repository
```bash
git clone https://github.com/jaiagosto/assignment9.git
cd assignment9
```

### 2. Start Docker Services

Build and start all containers:
```bash
docker-compose up --build
```

Wait for all services to start (~2 minutes). You should see:
- ✅ PostgreSQL database ready
- ✅ FastAPI app running on port 8000
- ✅ pgAdmin ready on port 5050

### 3. Access the Applications

- **FastAPI Calculator:** http://localhost:8000
- **pgAdmin:** http://localhost:5050
- **API Docs:** http://localhost:8000/docs

---

## 🔐 Login Credentials

### pgAdmin Login
- **Email:** `admin@example.com`
- **Password:** `admin`

### PostgreSQL Database
- **Host:** `db` (when connecting from pgAdmin)
- **Port:** `5432`
- **Database:** `fastapi_db`
- **Username:** `postgres`
- **Password:** `postgres`

---

## 🗄️ Database Setup in pgAdmin

### Step 1: Login to pgAdmin

1. Open http://localhost:5050
2. Login with email: `admin@example.com` and password: `admin`

### Step 2: Connect to PostgreSQL Server

1. Right-click **Servers** → **Register** → **Server**
2. **General Tab:**
   - Name: `FastAPI DB`
3. **Connection Tab:**
   - Host name/address: `db`
   - Port: `5432`
   - Maintenance database: `fastapi_db`
   - Username: `postgres`
   - Password: `postgres`
   - ✅ Check "Save password"
4. Click **Save**

### Step 3: Open Query Tool

1. Expand: **Servers** → **FastAPI DB** → **Databases** → **fastapi_db**
2. Right-click on `fastapi_db`
3. Select **Query Tool**

---

## 📝 SQL Operations

Run these SQL commands in pgAdmin Query Tool in order.

### A. Create Tables
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE calculations (
    id SERIAL PRIMARY KEY,
    operation VARCHAR(20) NOT NULL,
    operand_a FLOAT NOT NULL,
    operand_b FLOAT NOT NULL,
    result FLOAT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```

**Expected:** "Query returned successfully"

---

### B. Insert Records
```sql
INSERT INTO users (username, email) 
VALUES 
('alice', 'alice@example.com'), 
('bob', 'bob@example.com');

INSERT INTO calculations (operation, operand_a, operand_b, result, user_id)
VALUES
('add', 2, 3, 5, 1),
('divide', 10, 2, 5, 1),
('multiply', 4, 5, 20, 2);
```

**Expected:** "INSERT 0 2" and "INSERT 0 3"

---

### C. Query Data

#### Retrieve all users
```sql
SELECT * FROM users;
```

**Expected Result:**
| id | username | email | created_at |
|----|----------|-------|------------|
| 1 | alice | alice@example.com | [timestamp] |
| 2 | bob | bob@example.com | [timestamp] |

---

#### Retrieve all calculations
```sql
SELECT * FROM calculations;
```

**Expected Result:**
| id | operation | operand_a | operand_b | result | timestamp | user_id |
|----|-----------|-----------|-----------|--------|-----------|---------|
| 1 | add | 2 | 3 | 5 | [timestamp] | 1 |
| 2 | divide | 10 | 2 | 5 | [timestamp] | 1 |
| 3 | multiply | 4 | 5 | 20 | [timestamp] | 2 |

---

#### Join users and calculations
```sql
SELECT u.username, c.operation, c.operand_a, c.operand_b, c.result
FROM calculations c
JOIN users u ON c.user_id = u.id;
```

**Expected Result:**
| username | operation | operand_a | operand_b | result |
|----------|-----------|-----------|-----------|--------|
| alice | add | 2 | 3 | 5 |
| alice | divide | 10 | 2 | 5 |
| bob | multiply | 4 | 5 | 20 |

---

### D. Update a Record
```sql
UPDATE calculations
SET result = 6
WHERE id = 1;
```

**Expected:** "UPDATE 1"

Verify the update:
```sql
SELECT * FROM calculations WHERE id = 1;
```

---

### E. Delete a Record
```sql
DELETE FROM calculations
WHERE id = 2;
```

**Expected:** "DELETE 1"

Verify the deletion:
```sql
SELECT * FROM calculations;
```

**Expected:** Only 2 calculations remaining (id 1 and 3)

---

## 📸 Required Screenshots

Take screenshots of the following:

1. ✅ Docker containers running (`docker ps` output)
2. ✅ pgAdmin login page
3. ✅ PostgreSQL server connected in pgAdmin
4. ✅ CREATE TABLE execution and success message
5. ✅ INSERT statements execution
6. ✅ SELECT * FROM users result
7. ✅ SELECT * FROM calculations result
8. ✅ JOIN query result
9. ✅ UPDATE statement execution
10. ✅ DELETE statement execution
11. ✅ FastAPI calculator page at localhost:8000

---

## 🔄 Docker Commands

### Start services
```bash
docker-compose up --build
```

### Stop services
```bash
docker-compose down
```

### Stop and remove all data
```bash
docker-compose down -v
```

### View running containers
```bash
docker ps
```

### View logs
```bash
docker-compose logs
```

---

## 🧪 Database Relationships

- **One-to-Many:** One user can have many calculations
- **Foreign Key:** `calculations.user_id` references `users.id`
- **CASCADE DELETE:** Deleting a user removes all their calculations

---

## 📚 Project Structure
```
assignment9/
├── app/
│   ├── __init__.py
│   └── operations.py          # Calculator functions
├── templates/
│   └── index.html             # Web interface
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── docker-compose.yml         # Docker services config
├── Dockerfile
├── main.py                    # FastAPI application
├── requirements.txt
├── pytest.ini
├── .gitignore
└── README.md
```

---

## ✅ Assignment Checklist

- [ ] Docker Compose configured with PostgreSQL and pgAdmin
- [ ] All containers running successfully
- [ ] Connected to PostgreSQL in pgAdmin
- [ ] Created users and calculations tables
- [ ] Inserted sample data
- [ ] Queried data with SELECT statements
- [ ] Performed JOIN operation
- [ ] Updated a record
- [ ] Deleted a record
- [ ] Took all required screenshots
- [ ] Documented everything in Word/PDF
- [ ] Pushed code to GitHub

---

## 🎓 Learning Outcomes

This assignment demonstrates:
- ✅ Docker Compose multi-container setup
- ✅ PostgreSQL database integration
- ✅ SQL DDL operations (CREATE TABLE)
- ✅ SQL DML operations (INSERT, SELECT, UPDATE, DELETE)
- ✅ Database relationships (Foreign Keys, Joins)
- ✅ pgAdmin database management

---

## 📎 Links

- **GitHub Repository:** https://github.com/jaiagosto/assignment9
- **Docker Hub:** https://hub.docker.com/r/jaiagosto/assignment9

---

## 📄 License

MIT License - See LICENSE file for details

---

## 👩‍💻 Author

**Jailene Agosto**  
Assignment: Module 9 - Working with Raw SQL in pgAdmin