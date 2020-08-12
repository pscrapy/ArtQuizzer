#!/usr/bin/perl -w
use lib('lib/');  
use HTML::Template;
use Text::CSV qw( csv );


# Read whole file in memory
my $aoh = csv (in => "../data/imgdata.csv",
               headers => "auto", sep_char=> ";");   # as array of hash

my $sel = int(rand(37181));


# open the html template
my $template = HTML::Template->new(filename => 'template.html');
 
# fill in some parameters
$template->param(IMG=> $aoh->[$sel]{imgURL});
$template->param(AUTH=> $aoh->[$sel]{AUTHOR});
$template->param(PERIOD=> $aoh->[$sel]{TIMEFRAME});
$template->param(PLACE=> $aoh->[$sel]{LOCATION});
$template->param(TITLE=> $aoh->[$sel]{TITLE});
$template->param(DATE=> $aoh->[$sel]{DATE});
 
# send the obligatory Content-Type and print the template output
print "Content-Type: text/html\n\n", $template->output;
