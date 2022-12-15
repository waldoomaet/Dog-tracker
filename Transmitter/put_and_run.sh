#!/bin/bash

cd "source";

port=$1
for file in *; do
    if [[ $file != "main.py" ]]; then
        echo "Putting file $file"
        ampy --port $port put $file
    fi
done
echo "Starting the run..."
ampy --port $port run main.py