# To Create a /tmp file

file { '/tmp/school':
  path    => '/tmp/school',
  mode    => '0744',
  owener  => 'www-data'
  group   => 'www-data',
  content => 'I love Puppet',
  }
