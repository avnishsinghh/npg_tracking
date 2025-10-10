#!/usr/bin/perl

use strict;
use warnings;
use CGI;
use Carp qw(croak);

main();
exit 0;

sub main() {
        my $q = CGI->new;

        my $previous_url = $q->cookie('previous_url') 
                            || 'https://' . $ENV{HTTP_HOST} . '/perl/npg';

        my $clear_cookie = $q->cookie(
                            -name    => 'previous_url',
                            -value   => '', ## no critic (ValuesAndExpressions::ProhibitEmptyQuotes)
                            -expires => '-1d',
                            -path    => '/', ## no critic (ValuesAndExpressions::ProhibitNoisyQuotes)
                            -secure  => 0,
                            );

        print $q->redirect(-uri => $previous_url,
                            -cookie => $clear_cookie
                          ) or croak 'Failed to send redirect header.';
        return;
}
