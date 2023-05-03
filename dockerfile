# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /home/ec2-user/calc

# copy the content of the local directory to the working directory
COPY . /home/ec2-user/calc

# install dependencies
RUN pip install -r requirements.txt

# script to run on container start
RUN chmod a+x start.sh
CMD ./start.sh