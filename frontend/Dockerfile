FROM node:18-alpine

WORKDIR /app

# Install Quasar CLI globally
RUN npm install -g @quasar/cli

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 9000

CMD ["quasar", "dev", "--host", "0.0.0.0"]