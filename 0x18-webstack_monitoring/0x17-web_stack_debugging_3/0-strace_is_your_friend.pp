# Fixes typo in php extensions in Word Press config file `wp-settings.php`
exec { 'fix typo':
  command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/' /var/www/html/wp-settings.php",
  path    =>  '/bin:/usr/bin:/sbin:/usr/sbin:...'
}
