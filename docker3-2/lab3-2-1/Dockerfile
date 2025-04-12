FROM ruby:3.2

WORKDIR /app

# Install dependencies first
RUN apt-get update && \
    apt-get install -y default-mysql-client libmariadb-dev && \
    rm -rf /var/lib/apt/lists/*

# Copy Gemfiles first
COPY Gemfile Gemfile.lock ./

# Install gems
RUN bundle install --jobs=4 --retry=3

# Copy the rest of the app
COPY . .

EXPOSE 4567

CMD ["ruby", "app.rb"]