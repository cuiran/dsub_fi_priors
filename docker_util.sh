#!/bin/bash

git -C pyscripts/ pull origin master 

docker build -t fi-priors .
docker tag fi-priors gcr.io/finucane-dp5/fi-priors:latest
docker push gcr.io/finucane-dp5/fi-priors:latest
