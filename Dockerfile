# Use the official Node.js 14 image as the base image
FROM node:14

# Create and set the working directory
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the application code to the working directory
COPY app .

# Expose the port that the application will listen on
EXPOSE 3000

# Start the application
CMD [ "node", "index.js" ]
