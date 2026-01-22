FROM node:18-alpine
WORKDIR /app
COPY package.json /app/
RUN npm i
COPY src /app/src
CMD ["npx", "tsx", "src/index.ts"]
