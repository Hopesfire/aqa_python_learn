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
```

## Environment Variables

Create `.env` file based on `.env.example`:

```bash
cp .env.example .env
```

## Run Tests

```bash
pytest -q
```