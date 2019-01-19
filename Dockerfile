# Base image
FROM python:3.6

# Author information
MAINTAINER ruslan.rakhimov@skoltech.ru

# Set a working directory
WORKDIR homework

# Install necessary libraries
RUN pip install numpy scipy matplotlib imageio

# Add necessary files. Good practice to do it at the end
# in order to avoid reinstallation of dependencies when files change
ADD qr_code.jpg ./
ADD iip.py ./
ADD run.sh ./

# Make run.sh executable
RUN chmod +x run.sh

# /example/results contents will be shared with the host
# if -v option used with "docker run" command
VOLUME /homework/results

CMD ./run.sh

