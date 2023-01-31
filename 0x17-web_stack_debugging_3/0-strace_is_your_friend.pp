# Fix php server
# Creating needing files
$wpfiles = [ '/var/www/html/.maintenance',
          '/var/www/html/wp-content/languages',
          '/var/www/html/wp-content/db.php',
          '/var/www/html/wp-content/object-cache.php']

file { $wpfiles:
  ensure => 'present',
}

# copy wp needed from source
file { '/var/www/html/wp-includes/class-wp-locale.phpp':
  source => '/var/www/html/wp-includes/class-wp-locale.php'
}
