#!/bin/bash

cp -r /var/backups/app/* /app

python -B /app/run.py