#!/usr/bin/env bash
docker run -v $(pwd):/workspace -it -p 5000:5000 -e "FLASK_ENV=development" classification-test