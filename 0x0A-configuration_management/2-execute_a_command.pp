# create manifest that kills a procces name killmenow

exec { 'pkill':
  command  => 'pkill -f killmenow',
  provider => 'shell',
}
