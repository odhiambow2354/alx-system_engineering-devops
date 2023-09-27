# manifest for kill process kilmenow
exec { 'pkill':
command => 'pkill killmenow',
provider => 'shell',
}
