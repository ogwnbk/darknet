#!/usr/bin/perl

open (DARKNET_OUT, '</usr/lib/cgi-bin/darknet_out') or die "$!";

open (DARKNET_IN, '>/usr/lib/cgi-bin/darknet_in') or die "$!";
print DARKNET_IN "data/dog.jpg\n";
close (DARKNET_IN);

while(<DARKNET_OUT>){
	print $_;

	if($_ =~ /Complete!!/){
	      last;
	}
}

close (DARKNET_OUT);

1;