require 'sinatra'
require 'mysql2'

set :bind, '0.0.0.0'

get '/' do
  begin
    client = Mysql2::Client.new(
      host: ENV['MYSQL_HOST'],
      username: ENV['MYSQL_USER'],
      password: ENV['MYSQL_PASSWORD'],
      database: ENV['MYSQL_DATABASE'],
      reconnect: true
    )
    
    results = client.query('SELECT VERSION() as version')
    "MySQL version: #{results.first['version']}"
  rescue Mysql2::Error => e
    "Error connecting to MySQL: #{e.message}"
  end
end