FROM node:16.16.0-slim
WORKDIR /node
COPY package.json package.json
RUN npm install
COPY app.js app.js
EXPOSE 3000
CMD ["node", "app.js"]
