#!/bin/sh
echo "Running calc_csv.py"
python3 calc_csv.py
echo "Running traveling_salesman.py"
python traveling_salesman.py
pip install bandit
echo "Running Bandit"
/usr/bin/bandit *.py
cat results.txt
docker build -t calc .
docker run calc:latest
echo "Pushing docker image to Dockerhub"
id=$(docker images -q calc:latest)
echo ${DOCKER_PASSWORD} | docker login -u="${DOCKER_USERNAME}" --password-stdin
docker tag $id hydeb/calculator_app
docker push hydeb/calculator_app