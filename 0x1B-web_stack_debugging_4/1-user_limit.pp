# Changes user limit
exec { 'hard limit':
  path    => ['/bin'],
  command => 'sed -i "s/holberton hard nofile 5/holberton hard nofile 1024/" /etc/security/limits.conf',
}

exec { 'soft limit':
  path    => ['/bin'],
  command => 'sed -i "s/holberton soft nofile 4/holberton soft nofile 1024/" /etc/security/limits.conf',
}
