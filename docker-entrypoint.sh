#!/bin/bash

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Run makemigrations
echo "Collect static files"
python manage.py makemigrations --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

set -e

# first arg is `-f` or `--some-option`
# or first arg is `something.conf`
if [ "${1#-}" != "$1" ] || [ "${1%.conf}" != "$1" ]; then
	set -- redis-server "$@"
fi

# allow the container to be started with `--user`
# shellcheck disable=SC2166
if [ "$1" = 'redis-server' -a "$(id -u)" = '0' ]; then
	chown -R redis .
	exec gosu redis "$0" "$@"
fi

exec "$@"