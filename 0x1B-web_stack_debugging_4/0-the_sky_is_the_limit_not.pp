# Puppet manifest
exec { 'Hello':
  path    => ['/bin'],
  command => 'sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  notify  => Service['nginx'],
}
service { 'nginx':
  ensure => running,
  enable => true,
}
