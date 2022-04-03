#!/bin/bash
source venv/bin/activate
python ./app/data_insert.py
gunicorn -w 1 -b 0.0.0.0:8000 run:app