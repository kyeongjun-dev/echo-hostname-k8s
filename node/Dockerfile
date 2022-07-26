FROM node:16.16.0-slim
RUN apt update -y && apt install -y curl jq
WORKDIR /node
COPY package.json package.json
RUN npm install
COPY app.js app.js
EXPOSE 3000
CMD ["node", "app.js"]
