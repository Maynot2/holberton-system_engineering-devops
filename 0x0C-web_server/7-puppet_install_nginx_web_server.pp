# puppet manifest to install nginx and some redirects

package { 'nginx':
  ensure   => installed,
  provider => 'apt'
}

file { '/var/www/html/index.html':
  ensure  => present,
  path    => '/var/www/html/index.html',
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
  content => 'Holberton School for the win!'
}

$default_config = "server {
        listen 80 default_server;
        listen [::]:80 default_server;
        root /var/www/html;
        rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
        index index.html index.htm index.nginx-debian.html;
        server_name _;
        location / {
                try_files $uri $uri/ =404;
        }
}
"

file { '/etc/nginx/sites-available/default':
  ensure => present,
  path   => '/etc/nginx/sites-available/default'
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
  content => "$default_config"
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
