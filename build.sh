#!/bin/sh

# I put this in for consistency, so all developer utility scripts are run the
# same way
if [ "$0" = "$BASH_SOURCE" ]; then
    echo "Run this with source. (source build.sh, or . build.sh)"
    exit 1
fi

# build the database image
pushd src/docker/db-docker
sudo docker build -t mysqldb .
popd

# build the django image
pushd src/docker/django-docker
sudo docker build -t djangotest .
popd

# build the nodejs image
pushd src/docker/react-docker
sudo docker build -t react .
popd

# build the nodejs image
pushd src/docker/redis-docker
sudo docker build -t redis .
popd

sudo docker network create db-django-net

printf "\nTo run the docker containers, run:\n"
printf "    . run.sh\n"

printf "\nTo stop/remove/restart the docker containers, run:\n"
printf "    . rerun.sh\n"
