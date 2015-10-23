Title: “Headers already sent” error
Date: 2009-09-20
Category: Blog
Tags: wordpress, php
Summary: A quick note on avoiding a common error within WordPress

If you receive a PHP error similar to that above, you’ll need to enable output
buffering if you can. This can be done fairly simply by adding the following
line to your .htaccess file. (That lives in the root folder of your website:
    often named _/htdocs_, _/httpdocs_ or _/public_html_.)

```
php_value output_buffering 4096
```

This instructs PHP not to send data to the browser until the full page has been
read by the server. (Usually, PHP sends HTML to the browser, processes a PHP
    block when it comes to one, sends the next bit of HTML and so on.

If you try and instruct the browser to do something while it’s in this mode,
unless the instruction is right at the beginning, it’ll be too late, because the
browser’s already receiving data. Using the `output_buffering` setting means PHP
waits for the entire HTML page to be parsed before sending the resulting HTML to
the browser, with any instructions at the beginning of the page.)
