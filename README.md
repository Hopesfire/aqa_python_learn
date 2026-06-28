# AQA Python Learn

## Setup

Clone repository:

```bash
git clone https://github.com/Hopesfire/aqa_python_learn
cd aqa-python-learn
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
playwright install
```

## Environment Variables

Create `.env` file based on `.env.example`:

```bash
cp .env.example .env
```

| Variable | Description | Required |
|---|---|---|
| `GH_USER` | GitHub username | Yes (UI tests) |
| `GH_PASS` | GitHub password | Yes (UI tests) |

Without these variables UI login tests will be skipped automatically.

## How to Run UI Tests

Run all UI tests:
```bash
pytest -m ui
```

Run Playwright tests only:
```bash
pytest -m playwright
```

Run Selenium tests only:
```bash
pytest -m selenium
```

## Run Tests

```bash
pytest -q
```