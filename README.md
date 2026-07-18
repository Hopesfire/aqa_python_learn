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
| `REQRES_API_KEY` | Reqres API key | Yes (API tests) |
| `REQRES_EMAIL` | Reqres login email | Yes (API tests) |
| `REQRES_PASSWORD` | Reqres login password | Yes (API tests) |

Without 'GH_USER', 'GH_PASS' variables UI login tests will be skipped automatically.

Without 'REQRES_API_KEY' variable API tests will be skipped automatically.

## How to Run API Tests

Run all API tests:
```bash
pytest -m api
```

## How to Run UI Tests

Run all UI tests:
```bash
pytest -m ui
```
> **Note:** DuckDuckGo search tests may occasionally fail due to site unavailability.
> Skip with `pytest -m "ui and not duckduckgo"`

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
