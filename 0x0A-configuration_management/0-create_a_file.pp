# To Create a /tmp file

file { 'school':
  ensure  => 'present',
  content => 'I love Puppet',
  group   => 'www-data',
  mode    => '0744',
  owener  => 'www-data'
  path    => '/tmp/school',
}
