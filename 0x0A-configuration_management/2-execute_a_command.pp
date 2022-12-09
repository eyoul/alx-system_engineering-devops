# terminate killmenow

exec { 'pkill killmenow' :
    path    => '/bin/',
    command => 'pkill killmenow',
    }
