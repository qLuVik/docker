# Используем облегченный образ Ruby на базе Alpine
FROM ruby:3.0-alpine

# Устанавливаем зависимости для сборки Ruby-гемов и runtime-зависимости
RUN apk add --no-cache build-base gcompat

# Создаем рабочую директорию
WORKDIR /app

# Копируем Gemfile и устанавливаем зависимости
COPY Gemfile .
RUN bundle install --jobs $(nproc)

# Копируем основной файл приложения
COPY app.rb .

# Открываем порт, на котором работает Sinatra (по умолчанию 4567)
EXPOSE 4567

# Запускаем приложение с использованием Puma
CMD ["bundle", "exec", "ruby", "app.rb", "-s", "puma"]
