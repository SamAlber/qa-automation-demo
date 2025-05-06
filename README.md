# 🧪 QA Automation Demo Project (Flask API + Pytest + Docker Compose)

This project demonstrates a real-world **QA Automation testing workflow** using:

- 🐍 **Flask** — a simple REST API for `/login`
- ✅ **Pytest** — for writing automated tests
- 🐳 **Docker + Docker Compose** — containerized app + tests
- 🔄 **GitHub Actions CI** — running tests automatically on each push

---

## 📂 Project Structure

```
.
├── app/
│   ├── login.py              # Flask API logic
│   └── Dockerfile            # Container for the Flask app
│
├── tests/
│   ├── test_login.py         # Pytest cases
│   └── Dockerfile            # Container for running tests
│
├── requirements.txt          # Shared dependencies for both images
├── docker-compose.yml        # Runs app and tests together
├── .github/workflows/
│   └── pytest.yml            # GitHub Actions CI
└── README.md                 # You are here
```

---

## 🚀 What This Project Demonstrates

✅ **A working, non-trivial test pipeline** for a web API.

✅ **Containerized separation** between the app and its tests.

✅ **Docker Compose orchestration** that simulates production-like integration testing.

✅ **GitHub CI pipeline** that builds images, runs tests, and optionally runs security scans.

---

## 🧠 Why We Did What We Did (Project Evolution Explained)

### Phase 1 — Monolithic Image With App + Tests

- At first, I put the tests and the app into the **same Docker image**.
- I ran `pytest` after the container booted using `sh -c "sleep 5 && pytest"`.
- ✅ This worked, but it felt **non-modular and less professional**.

### Phase 2 — Separate Docker Images

- I splited the app and test logic into **two clean Dockerfiles**:
  - `app/Dockerfile` runs `login.py`.
  - `tests/Dockerfile` installs `pytest` and runs the test suite.
- The **test container depends on the app container** in `docker-compose.yml`.

### Phase 3 — Docker Compose

- Using Docker Compose gave me better orchestration:
  - **Shared network**, like Kubernetes pods
  - Parallel container lifecycles
- The `test` service waits for the `app` to be ready.

### Phase 4 — CI Integration with GitHub Actions

- On every push, GitHub:
  - Builds both containers
  - Brings them up via `docker-compose`
  - Runs tests

---

## 🔁 CI/CD Considerations

- In real QA workflows
  - Devs build the app + write tests in the same repo
  - QA writes additional tests and plugs them into CI
  - Docker Compose is commonly used for **integration testing**
  - Some orgs use Kubernetes or test orchestrators (e.g. Testcontainers) in advanced setups

---

## ⚠️ .dockerignore — Do We Still Need It?

Earlier, when we had a **single Dockerfile**, we used `.dockerignore` to exclude:

```
.dockerignore
.git/
__pycache__/
tests/
```

Why?

- To avoid copying unnecessary files into the Docker image.
- To **make the image lean and build faster**.

### Now?

- Since the app and tests are **in separate Docker images**, the tests are **only copied into the test container**.
- The `.dockerignore` is now **optional**, but still useful to **avoid bloated contexts** during `docker build`.

✅ Verdict: **I will Keep it** and tailor it per directory (`app/`, `tests/`) if needed.

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

### 3. Run tests manually (if app is already running):

```bash
pytest -v tests/
```

---

## ✅ Example Test Cases

- ✅ Successful login with correct credentials
- ❌ Failed login with wrong credentials
- 🚫 Request with missing fields
- ❌ Request with no JSON payload

---

## 🏗️ Technologies Used

- Python 3.11
- Flask
- Pytest
- Docker
- Docker Compose
- GitHub Actions CI
- Optional: Trivy for security scanning

---

## 💬 Final Thoughts

This project is a compact simulation of **how real QA engineers validate APIs**:

- With real tests
- In isolated, reproducible environments
- Using modern CI/CD tools

---

🧑‍💻 Author
Samuel Albershtein
📫 www.samuelalber.com
