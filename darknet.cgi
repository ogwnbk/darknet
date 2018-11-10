#!/usr/bin/perl

use CGI;
use File::Copy;

$cgi = new CGI;
print "Content-type: text/html\n\n";

if($ENV{'REQUEST_METHOD'} =~ /GET/){
    print<<EOM
<html>
	<head>
	  <title>darknet demo</title>
	</head>
	<body>
<form enctype="multipart/form-data" method=post>
  <input type="file" name="upfile">
  <input type="submit" value="upload">
</form>
	</body>
</html>

EOM
}elsif($ENV{'REQUEST_METHOD'} =~ /POST/){
    my $upfile = $cgi->param('upfile');
    my $tmpfile = $cgi->tmpFileName($upfile);
    my $upload_file_path = "/var/www/html/upload.jpg";
    File::Copy::copy($tmpfile, $upload_file_path);
    
    open (DARKNET_OUT, '</usr/lib/cgi-bin/darknet_out') or die "$!";
	
    open (DARKNET_IN, '>/usr/lib/cgi-bin/darknet_in') or die "$!";
    #print DARKNET_IN "data/dog.jpg\n";
    print DARKNET_IN "$upload_file_path\n";
    close (DARKNET_IN);

    print "<img src=\"/upload.jpg\" width=\"400px\">\n";
    print "<img src=\"/predictions.jpg\" width=\"400px\"><br>\n";

    print "<pre>\n";
    while(<DARKNET_OUT>){
	print $_;
	
	if($_ =~ /Complete!!/){
	    last;
	}
    }
    print "</pre>\n";
    
    close (DARKNET_OUT);
}

1;
