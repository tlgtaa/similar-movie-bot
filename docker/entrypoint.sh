#!/bin/bash

set -e

python /proj/docker/connectpg.py "$DATABASE_URL" && exec "$@"
