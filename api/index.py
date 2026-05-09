"""Vercel entrypoint for the Dash dashboard.

Vercel's Python runtime looks for a WSGI/ASGI variable named ``app`` in
``api/*.py``. The main project entrypoint creates a Dash app and exposes its
Flask server as ``server``; export that server here for Vercel Functions.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app import server as app
