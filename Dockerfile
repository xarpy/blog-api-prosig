# # Base on offical Python Slim image
FROM python:3.12.11-slim
# Set working directory
WORKDIR /api
# Copy all files
COPY . .
# Install dependencies
RUN pip install --require-hashes -r /api/requirements/dev.txt
