exec { 'kill killmenow':
  command => 'pkill -15 killmenow',
  path    => '/usr/bin/'
}
