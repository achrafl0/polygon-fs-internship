FROM node:13.8.0-buster
WORKDIR /polygon-perf-front
COPY package.json .
RUN yarn install
COPY . .
EXPOSE 8080
CMD ["yarn", "run", "serve"]
