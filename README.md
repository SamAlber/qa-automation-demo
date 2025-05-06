# 🧪 QA Automation Demo — Flask Login API

This project demonstrates a simple **automated QA workflow** using:

- 🐍 Python + Flask API
- ✅ Pytest test suite
- 🐳 Docker & Docker Compose
- 🔁 GitHub Actions CI

It was created to simulate a **real-world QA testing flow**.

---

## 🔧 What This Project Does

- Provides a minimal **Flask API** (`login.py`) with a `/login` endpoint.
- Implements **realistic integration tests** using `pytest` (`test_login.py`).
- Uses **Docker Compose** to run:
  - A container for the app
  - A container that waits for the app, then runs tests against it
- Supports **GitHub Actions CI** that:
  - Builds the app container
  - Runs the tests via Docker Compose with the app container as a host and another container as a client to send HTTP requests. 

---

## 📂 Project Structure

qa-automation-demo/
├── app/
│ └── login.py # The Flask API app
├── tests/
│ └── test_login.py # Pytest test suite for the API
├── Dockerfile # Builds the testable app image
├── docker-compose.yml # Defines app + test containers
├── requirements.txt # Python dependencies
└── .github/workflows/ci.yml # GitHub Actions pipeline

---

## 🚀 Why Docker & Docker Compose?

We needed a way to:

1. **Start the app in a reproducible container**.
2. **Run tests against it** while it's alive.
3. Ensure this works **both locally and in CI** (GitHub Actions).

Docker Compose allowed us to **spin up both the app and the test runner** in a single command:

```bash
docker compose up --build --abort-on-container-exit
```

---

🧑‍💻 Author
Samuel Albershtein
📫 www.samuelalber.com
