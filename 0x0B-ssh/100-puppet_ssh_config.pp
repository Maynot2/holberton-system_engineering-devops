# Create custom config file

file_line {'disable password authentification':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no'
}

file_line { 'Change default path to private key':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/holberton'
}

file_line { 'Change default path to private key':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentitiesOnly yes'
}
