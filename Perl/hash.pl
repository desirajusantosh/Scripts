#Init a hash
my %hash = ();

#Init a hash ref
my $hash_ref = {};

#clear or empty hash
for (keys %hash) {
  delete $hash($_);
}

#clear or empty hash ref
for (keys %$hash_ref) {
  delete $hash_ref->($_);
}  
