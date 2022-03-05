#!/bin/bash
docker rm -f web_pat_pat_generator
docker build -t web_pat_pat_generator .
docker run --name=web_pat_pat_generator --rm -p1337:1337 -it web_pat_pat_generator