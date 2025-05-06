# 🧪 QA Automation Demo Project (Flask API + Pytest + Docker Compose)

This project demonstrates a real-world **QA Automation testing workflow** using:

- 🐍 **Flask** — a simple REST API for `/login`
- ✅ **Pytest** — for writing automated tests
- 🐳 **Docker + Docker Compose** — containerized separation between app and its tests (simulates production-like integration testing.)
- 🔄 **GitHub Actions CI** — running tests automatically on each push

---

## 📂 Project Structure

```
.
├── app/
│   └── login.py              # Flask API logic
│
├── tests/
│   └── test_login.py         # Pytest cases
│
├── Dockerfile.app            # Container for the Flask app
│
├── Dockerfile.test           # Container for running tests
│
├── requirements.txt          # Shared dependencies for both images
│
├── docker-compose.yml        # Runs app and tests together
│
├── .github/workflows/
│   └── pytest.yml            # GitHub Actions CI
│
└── README.md                 # You are here
```

---

## 🚀 What This Project Demonstrates

✅ A working, non-trivial test pipeline for a web API.  
✅ Containerized separation between the app and its tests.  
✅ Docker Compose orchestration that simulates production-like integration testing.  
✅ GitHub CI pipeline that builds images, runs tests, and optionally runs security scans.  

---

## 🧠 Why We Did What We Did (Project Evolution Explained)

### Phase 1 — Monolithic Image With App + Tests

- Initial design: app and tests in a **single container**.
- Ran `pytest` after `sleep 5` inside `sh -c` entrypoint.
- ✅ Worked, but not scalable, not clean, and not modular.

### Phase 2 — Separate Docker Images

- I splited the app and test logic into **two clean Dockerfiles**:
  - `app/Dockerfile` runs `login.py`.
  - `tests/Dockerfile` installs `pytest` and runs the test suite.
- The **test container depends on the app container** in `docker-compose.yml`.

### Phase 3 — Separate Docker Images (Best Practice)

- Split the logic into two Dockerfiles:
  - `Dockerfile.app` for Flask app
  - `Dockerfile.test` for Pytest
- Better reflects **real-world separation of concerns**.
- Enables **test failures to be caught earlier and independently**.

### Phase 4 — Docker Compose

- Containers run in the same network — like Kubernetes pods.
- Test container starts only **after app is up** (`depends_on`).
- Uses `docker compose up --abort-on-container-exit` for CI-style behavior.

### Phase 5 — GitHub Actions CI

- On every push to `main`, GitHub:
  - Builds both containers
  - Starts them with Compose
  - Tests run inside `test` container
  - Optionally scans the image with Trivy

---

## 🔁 CI/CD Considerations

- In QA/DevOps:
  - Devs push to GitHub → Tests run automatically
  - QA may write test cases and contribute to coverage
  - Teams often **protect the `main` branch** (merge only if tests pass)

---

## 🔒 Branch Protection & Production Readiness

- We **protected the main branch** to block pushes if tests fail.
- Can add additional approvals for merge, or PR-only workflows.
- This reflects how **production teams use CI/CD responsibly**.

---

## ⚠️ `.dockerignore` — Do We Still Need It?

### 🕰️ Earlier Setup (Dockerfiles Inside `app/` and `tests/`)

- We had Dockerfiles under `./app` and `./tests`, so the build context was limited.
- Docker only saw files within those folders — not the whole project.
- `.dockerignore` was **not strictly needed**.

### 📦 Current Setup (Dockerfiles in Root)

- Dockerfiles are in the root.
- Build context is `.` (the entire project directory).

❌ This means **everything** (like `.git`, `tests/`, `.vscode`, etc.) is sent during the build unless excluded.

✅ We now **do need `.dockerignore`** again to avoid bloated images and slower builds.

---

## ▶️ How to Run Locally

### 1. Run the full test suite:

```bash
docker compose up --build --abort-on-container-exit
```

### 2. Run only the Flask app:

```bash
docker compose up app
```

### 3. Run tests manually:

```bash
docker compose run --rm test
```

---

## ✅ Example Test Cases

- ✅ Valid login
- ❌ Invalid credentials
- 🚫 Missing fields
- ⛔ No payload (triggering 400 errors depending on implementation)

---

## 🏗️ Technologies Used

- Python 3.11
- Flask
- Pytest
- Docker / Docker Compose
- GitHub Actions CI
- Trivy (optional)

---

## 💬 Final Thoughts

This project simulates a production-like QA flow:

- CI builds clean Docker images
- Docker Compose orchestrates test environment
- Tests validate logic in a real HTTP setting
- Protecting `main` ensures code quality

🧑‍💻 Author  
Samuel Albershtein  
📫 www.samuelalber.com