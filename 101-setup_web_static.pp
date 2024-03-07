# Define package to ensure Nginx is installed
package { 'nginx':
  ensure => installed,
}

# Define directories to be created
$folders_to_create = [
  '/data/',
  '/data/web_static/',
  '/data/web_static/releases/',
  '/data/web_static/shared/',
  '/data/web_static/releases/test/',
]

# Create necessary directories if they don't exist
file { $folders_to_create:
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Create an HTML file with fake content to test configuration
file { '/data/web_static/releases/test/index.html':
  ensure  => present,
  content => '<html>\n\t<head>\n\t</head>\n\t<body>\n\t\t<h1>Hello Ms Aevy </h1>\n\t</body>\n</html>',
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

# Create or recreate symbolic link
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test/',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Update Nginx configuration
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "server {\n    listen 80;\n    listen [::]:80;\n    server_name aevycreations.tech;\n\n    location /hbnb_static/ {\n        alias /data/web_static/current/;\n    }\n}\n",
  owner   => 'root',
  group   => 'root',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Ensure Nginx service is running
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

