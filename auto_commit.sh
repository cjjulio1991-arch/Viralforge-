#!/bin/bash

cd ~/ViralForge

python social_engine.py
python reels_engine.py

git add -A

git commit -m "ULTRA batch $(date '+%Y-%m-%d %H:%M:%S')" || echo "no changes"

git push
