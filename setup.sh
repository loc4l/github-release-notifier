#!/bin/bash

echo "📦 Installing required Python packages..."
pip install -r requirements.txt

echo "🚀 Running GitHub Release Notifier..."
python main.py