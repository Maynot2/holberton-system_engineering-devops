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

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
