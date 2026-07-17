#!/usr/bin/perl
use strict;
use warnings;
use CGI;
use Carp qw(croak);

my $cgi    = CGI->new;
my $action = $cgi->param('action') || 'login';

if ($action eq 'logout') {
  my $post_logout = 'https://' . $ENV{HTTP_HOST} . '/perl/npg';
  print $cgi->redirect(
    -uri => '/callback?logout=' . $post_logout,
  ) or croak 'Failed to send redirect header.';
}
else {
  print $cgi->redirect(
    -uri => '/perl/npg'
  ) or croak 'Failed to send redirect header.';
}
