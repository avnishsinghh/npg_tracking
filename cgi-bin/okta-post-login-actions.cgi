#!/usr/bin/perl

use strict;
use warnings;
use CGI;
use Carp qw(croak);
use Readonly;

Readonly::Scalar my $COOKIE_DOMAIN => '.sanger.ac.uk';
Readonly::Scalar my $SECURE_COOKIE => 0;
Readonly::Scalar my $COOKIE_PATH   => '/'; ## no critic (ValuesAndExpressions::ProhibitNoisyQuotes)

main();
exit 0;

sub main {
        my $q = CGI->new;
        my $previous_url = $q->cookie('previous_url')
                           || 'https://' . $ENV{HTTP_HOST} . '/perl/npg';

        perform_post_okta_login_actions($q, $previous_url);

        return;
}

sub clear_cookie {
        my ($q, $name) = @_;

        return $q->cookie(
                -name    => $name,
                -value   => '', ## no critic (ValuesAndExpressions::ProhibitEmptyQuotes)
                -expires => '-1d',
                -path    => $COOKIE_PATH,
                -secure  => $SECURE_COOKIE,
        );
}

sub perform_post_okta_login_actions {
        my ($q, $previous_url) = @_;

        if (!$ENV{'REMOTE_USER'}) {
                print $q->header(-status => '401 Unauthorized')
                        or croak 'Authentication required';
                exit;
        }

        print $q->redirect(
                -uri    => $previous_url,
                -cookie => [clear_cookie($q, 'previous_url')]
        ) or croak 'Failed to send redirect header.';
        return;
}
