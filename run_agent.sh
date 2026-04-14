#!/data/data/com.termux/files/usr/bin/bash

cd $HOME/ViralForge

while true
do
    echo "🚀 Ejecutando agente..."
    python main.py >> logs.txt 2>&1

    echo "⏳ Esperando 5 minutos..."
    sleep 300
done
