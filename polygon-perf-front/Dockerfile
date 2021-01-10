FROM node:13.8.0-buster
WORKDIR /polygon-perf-front
COPY package.json .
RUN yarn install
COPY . .
EXPOSE 8080
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.7.3/wait /wait
# We are adding the wait dependency here so we can wait out our db 
RUN chmod +x /wait
