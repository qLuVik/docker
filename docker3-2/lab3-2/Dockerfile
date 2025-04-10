# Используем официальный образ Node.js
FROM node:slim

# Создаем рабочую директорию
WORKDIR /usr/src/app

# Копируем package.json и package-lock.json
COPY package*.json ./

# Устанавливаем зависимости
RUN npm install

# Копируем остальные файлы
COPY . .

# Открываем порт, который будет использовать приложение
EXPOSE 3000

# Запускаем приложение
CMD ["node", "server.js"]