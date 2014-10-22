#!/usr/bin/perl -w
$_ = lc join(' ', <>);
s/[^a-z1-90.,:;?!(){}<> ]//g;
#s/([\w']+)/\u\L$1/g;
print;
