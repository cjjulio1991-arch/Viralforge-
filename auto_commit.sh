#!/bin/bash

cd ~/ViralForge

git add -A

git commit -m "auto update $(date '+%Y-%m-%d %H:%M:%S')" || echo "no changes"

git push
