Title: Weekday redirect
Date: 2009-09-19
Category: Projects
Tags: wordpress, php
Summary: Redirects to a specific page for each day of the week

This is a WordPress plugin created to redirect to a given page on a particular
day. Let’s say you want certain information to be available on a certain day,
like a list of events. Users could go to `http://yoursite.com/events`, which
would then redirect to `http://yoursite.com/events/<day>`, where `<day>` is
obviously “monday”, “tuesday” etc, depending on what day of the week it is.

There may already be more elegant solutions to this problem, but I wanted to
build a WordPress plugin from scratch, rather than adapting an existing one. The
much more efficient shortcodes system implemented in WordPres 2.5 (better than
lots of plugins performing a find and replace or regular expression check) makes
this really easy.

<a class="btn" href="https://wordpress.org/plugins/weekday-redirect/">
    <span class="octicon octicon-cloud-download"></span>
    Install it from WordPress
</a>
