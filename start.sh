#!/bin/bash
# Fitness Hub - One-Click Startup Script
# Works on Linux, macOS, and Git Bash (Windows)

set -e

echo ""
echo "  ╔═══════════════════════════════════════╗"
echo "  ║        Fitness Hub - Starting         ║"
echo "  ╚═══════════════════════════════════════╝"
echo ""

# ── Navigate to script directory ──
cd "$(dirname "$0")" 2>/dev/null || cd "$(pwd)"

# ── Check Python ──
PYTHON=""
for cmd in python3 python; do
    if command -v "$cmd" &> /dev/null; then
        PYTHON="$cmd"
        break
    fi
done

if [ -z "$PYTHON" ]; then
    echo "  [ERROR] Python is not installed."
    echo "  Install it from: https://www.python.org/downloads/"
    exit 1
fi

PY_VERSION=$($PYTHON --version 2>&1)
echo "  Using $PY_VERSION"

# ── Create virtual environment ──
if [ ! -d "venv" ]; then
    echo "  [1/5] Creating virtual environment..."
    $PYTHON -m venv venv
else
    echo "  [1/5] Virtual environment found."
fi

# ── Activate ──
echo "  [2/5] Activating virtual environment..."
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
elif [ -f "venv/Scripts/activate" ]; then
    source venv/Scripts/activate
else
    echo "  [ERROR] Could not find venv activation script."
    exit 1
fi

# ── Upgrade pip silently ──
python -m pip install --upgrade pip -q 2>/dev/null

# ── Install dependencies ──
echo "  [3/5] Installing dependencies..."
pip install -r requirements.txt -q

# ── Run migrations ──
echo "  [4/5] Setting up database..."
python manage.py migrate --run-syncdb 2>/dev/null || python manage.py migrate

# ── Seed sample data ──
EXERCISE_COUNT=$(python -c "from exercises.models import Exercise; print(Exercise.objects.count())" 2>/dev/null || echo 0)
if [ "$EXERCISE_COUNT" = "0" ]; then
    echo "  [5/5] Loading sample data..."
    python seed_data.py
else
    echo "  [5/5] Sample data already loaded."
fi

echo ""
echo "  ╔═══════════════════════════════════════════════╗"
echo "  ║  Fitness Hub is running!                      ║"
echo "  ║                                               ║"
echo "  ║  Open in browser:  http://localhost:8000       ║"
echo "  ║  Admin panel:      http://localhost:8000/admin ║"
echo "  ║                                               ║"
echo "  ║  Press Ctrl+C to stop the server              ║"
echo "  ╚═══════════════════════════════════════════════╝"
echo ""

python manage.py runserver 0.0.0.0:8000
