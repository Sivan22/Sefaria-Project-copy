# Use an official Python runtime as a parent image
FROM python:3.7-slim

# --- NETFREE CERT INTSALL ---
ADD https://netfree.link/dl/unix-ca.sh /home/netfree-unix-ca.sh 
RUN cat  /home/netfree-unix-ca.sh | sh
ENV NODE_EXTRA_CA_CERTS=/etc/ca-bundle.crt
ENV REQUESTS_CA_BUNDLE=/etc/ca-bundle.crt
ENV SSL_CERT_FILE=/etc/ca-bundle.crt
# --- END NETFREE CERT INTSALL ---

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install psycopg2 dependencies
RUN apt-get update && apt-get install -y libpq-dev

# Install gcc
RUN apt-get update && apt-get install -y gcc

# Install git
RUN apt-get update && apt-get install -y git

RUN $ curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf | sh


# Install git
RUN apt-get update && apt-get install -y cargo

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME Sefaria-Project

# Run app.py when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
