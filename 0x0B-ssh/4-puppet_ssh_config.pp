# Create custom config file

file { '/etc/ssh/ssh_config':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  mode    => '0644',
  owner   => 'root',
  group   => 'root'
  content => '
    dentityFile ~/.ssh/holberton
    IdentitiesOnly yes
    PasswordAuthentication no
    SendEnv LANG LC_*
    HashKnownHosts yes
    GSSAPIAuthentication yes
    GSSAPIDelegateCredentials no
ServerAliveInterval 120'
}
