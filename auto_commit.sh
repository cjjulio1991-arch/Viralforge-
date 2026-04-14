#!/bin/bash

cd ~/ViralForge

python viral_engine.py

git add -A

git commit -m "viral content $(date '+%H:%M:%S')" || echo "no changes"

git push
