FROM node:13.8.0-buster
WORKDIR /polygon-perf-front
COPY package.json .
RUN npm install
COPY . .
EXPOSE 8080
CMD ["npm", "run", "serve"]
