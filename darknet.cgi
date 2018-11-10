#!/usr/bin/perl

use CGI;
use File::Copy;

$cgi = new CGI;
print "Content-type: text/html\n\n";

if($ENV{'REQUEST_METHOD'} =~ /GET/){
    &print_header();
    &print_body();
    &print_footer();
}elsif($ENV{'REQUEST_METHOD'} =~ /POST/){
    &print_header();
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
    &print_footer();
}

sub print_header()
{
    print<<EOM
<!DOCTYPE html>
<html lang="en">
<head>
	<title>Contact V10</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
<!--===============================================================================================-->
	<link rel="icon" type="image/png" href="/images/icons/favicon.ico"/>
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="/vendor/bootstrap/css/bootstrap.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="/fonts/font-awesome-4.7.0/css/font-awesome.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="/vendor/animate/animate.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="/vendor/css-hamburgers/hamburgers.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="/vendor/animsition/css/animsition.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="/vendor/select2/select2.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="/vendor/daterangepicker/daterangepicker.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="/css/util.css">
	<link rel="stylesheet" type="text/css" href="/css/main.css">
<!--===============================================================================================-->
</head>
<body>
EOM
}

sub print_footer()
{
    print<<EOM
	<div id="dropDownSelect1"></div>

<!--===============================================================================================-->
	<script src="/vendor/jquery/jquery-3.2.1.min.js"></script>
<!--===============================================================================================-->
	<script src="/vendor/animsition/js/animsition.min.js"></script>
<!--===============================================================================================-->
	<script src="/vendor/bootstrap/js/popper.js"></script>
	<script src="/vendor/bootstrap/js/bootstrap.min.js"></script>
<!--===============================================================================================-->
	<script src="/vendor/select2/select2.min.js"></script>
<!--===============================================================================================-->
	<script src="/vendor/daterangepicker/moment.min.js"></script>
	<script src="/vendor/daterangepicker/daterangepicker.js"></script>
<!--===============================================================================================-->
	<script src="/vendor/countdowntime/countdowntime.js"></script>
<!--===============================================================================================-->
	<script src="/js/main.js"></script>

</body>
</html>

<!--
<form >
  <input type="file" name="upfile">
  <input type="submit" value="upload">
</form>
-->
EOM
}

sub print_body()
{
    print<<EOM
	<div class="container-contact100">

		<div class="wrap-contact100">
			<form class="contact100-form" enctype="multipart/form-data" method=post>
				<span class="contact100-form-title">
					Image Analysis
				</span>

				<div class="wrap-input100">
                                        <input type="file" name="upfile">
					<span class="focus-input100"></span>
				</div>

				<div class="container-contact100-form-btn">
					<button class="contact100-form-btn">
						<span>
							<i class="fa fa-paper-plane-o m-r-6" aria-hidden="true"></i>
							Send
						</span>
					</button>
				</div>
			</form>
		</div>
	</div>
EOM
}

1;
