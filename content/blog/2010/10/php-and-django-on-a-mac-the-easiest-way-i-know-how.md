Title: PHP and Django on a Mac, the easiest way I know how
Date: 2010-10-03
Category: Blog
Tags: php, django, osx, mysql
Summary: The story of how I got PHP, Django, Apache and MySQL working natively
on my Mac

I work primarily with two frameworks: WordPress (if you can call it a framework)
and Django. Therefore I want my Mac to be able to handle both, and preferably via
the same machinery. The Django development server's pretty good, but has some
limitations: it can only process one request at a time, which is fine if you're
doing basic work, but if you have AJAX calls that rely on other calls to the
same domain for example, you'll be left hanging.

I have a growing multisite content management system called [Dolphy](/projects/django/dolphy/), which runs on Apache with mod_wsgi (still
the best way to serve Django, via perhaps nginx, which I know next to nothing
about). It then makes sense for me to test using Apache, so I can get as close
to a real production environment as possible.

This is how today, I setup my machine, to run Apache 2, PHP5, MySQL5,
phpMyAdmin, Python 2.6 and some other goodies. The only downside to the
following setup is that I can't find a GUI to do the fiddly things like creating
new VirtualHost configs and setting the local domains in my hosts file.

Before you start, make sure Web Sharing is not in use. Go to System
Preferences > Sharing, and untick Web Sharing. Also, if like me you've been
using MAMP, delete (or move) it, then stop Apache and MySQL from running:

```sh
sudo killall httpd sudo killall mysqld
```

### MacPorts

Download and install MacPorts: <http://www.macports.org/install.php>

Make sure you have the latest list of ports:

```sh
sudo port self update
```

If any updates have been made, you can upgrade outdated packages with this
command:

```sh
sudo port upgrade outdated
```

### Apache and MySQL

If you do more than just Django, and if you want an easy way to manage your
databases, phpMyAdmin is a good way to go. For that you'll need PHP. But first,
Apache and MySQL.

```sh
sudo port install apache2 mysql5 +server
```

When I did this, MacPorts didn't install MySQL 5 Server, so I ran the following,
and within a flash, it did.

```sh
sudo port install mysql5-server
```

To load MySQL when the server starts:

```sh
sudo port load mysql5-server
```

If you already have MySQL installed - if you haven't installed it yourself, and
you've not installed anything like MAMP, chances are you don't - you can look
into removing it, to save confusion. I googled 'osx uninstall mysql' and
followed some instructions, but I won't link to them as that one's up to you :)

Install the necessary databases for MySQL to work:

```sh
sudo /opt/local/lib/mysql5/bin/mysql_install_db --user=mysql
```

Open your bash profile in one of the in-built UNIX text editors:

```sh
nano ~/.profile
```

and add the following lines:

```sh
alias mysqlstart='sudo /opt/local/bin/mysqld_safe5 &amp;' alias mysqlstop='/opt/local/bin/mysqladmin5 -u root -p shutdown' alias apache2ctl='sudo /opt/local/apache2/bin/apachectl'
```

This allows you to use the commands mysqlstart and mysqlstop to start and stop
MySQL, and apache2ctl to start and stop Apache. Nice!

Reload your bash profile:

```sh
source ~/.profile
```

and with any luck, Apache should already be running and you can run the
following to start up MySQL:

```sh
mysqlstart
```

Now set a root password for your MySQL installation. phpMyAdmin needs this in
place (unless you want to configure phpMyAdmin to allow the root user to login
    without a password, but that's out of scope):

```sh
mysqladmin5 -u root -p password <your-password>;
```

When prompted for a password, just press Enter (you shouldn't have one already).
Where you see the word "password" above, just after the -p, that's not a prompt,
but a literal word. What you're doing here is telling MySQL to set a password;
put your desired password where the bracketed bits go (removing the brackets
aswell). Now anytime you shut down your MySQL server using mysqlstop, you'll be
prompted for your root password. You'll also need it for phpMyAdmin.

Now to load Apache when the Mac starts:

```sh
sudo port load apache2
```

### PHP and MySQL

At the time of writing, the MySQL extension for PHP5 would not compile, due I
think to it not having been updated for the latest version of PHP (5.3.3). For
now, to get around this issue, you'll need to download the latest 5.3.2 release
of the PHP5 port.

We'll use Subversion to check this in to your Downloads directory. If you don't
have Subversion, you can use the following command to install it (it's a good
thing to have on your machine):

```sh
sudo port install subversion
```

So let's check out the penultimate version of this port into a folder called
macports-php5, within our Downloads directory (once this is all over, you can
delete this directory).

```sh
cd /opt/local/var/macports/sources/rsync.macports.org/release mv ports ports-bak svn co -r70350 http://svn.macports.org/repository/macports/trunk/dports ports cd ports sudo portindex sudo port install +apache2 +pear
```

This should be a temporary measure, and I hope that in a few days PHP5 will be
updatable to the latest version, but until then, keep your eye on
[ticket 26000](http://trac.macports.org/ticket/26000) on the MacPorts Trac. In
which case, I'll update this post.

What you've installed is PHP 5, the Apache module and Pear, the PHP extension
manager.

Hopefully this has all worked (if not, I'm really sorry, but please feel free to
post a comment. If I can find the answer, I will, and if you do, it'd be great
to hear from you). Now we can install the MySQL extension for PHP, along with
phpMyAdmin.

Enable the php.ini configuration file and the PHP5 Apache module:

```sh
sudo cp /opt/local/etc/php5/php.ini-development /opt/local/etc/php5/php.ini cd /opt/local/apache2/modules sudo /opt/local/apache2/bin/apxs -a -e -n "php5" libphp5.so sudo port install php5-mysql
```

As instructed, open /opt/local/etc/php5/php.ini and set the options
mysql.default_socket, mysqli.default_socket and pdo_mysql.default_socket to /opt/local/var/run/mysql5/mysqld.sock.

I'd also recommend finding the upload_max_filesize setting, and changing it to
something sensible. As it's a development machine, I'll go for 100M, giving me
plenty of headroom.

Now we can install phpMyAdmin.

```sh
sudo port install phpmyadmin
```

Open the following file in your text editor: /opt/local/apache2/conf/httpd.conf.
Near the bottom you'll see a line which reads:

```
#Include conf/extra/httpd-vhosts.conf
```

Uncomment that line (remove the hash symbol at the front). Then look for the
following:

```
<IfModule dir_module> DirectoryIndex index.html </IfModule>
```

and replace the DirectoryIndex line so it looks like this:

```
DirectoryIndex index.html index.php
```

Next, look for a block like this:

```
<IfModule mime_module> ... </IfModule>
```

And add the following lines, before the closing IfModule tag:

```
AddType application/x-httpd-php .php AddType application/x-httpd-php-source .phps
```

Save the file. You'll probably need to provide your password to do so.

This allows us to define all our virtual hosts (our sites) in a file called httpd-vhosts.conf. In turn, you can then set that file up to include lots of
other files if you want (a little like Ubuntu Apache's sites-enabled and
sites-available setup), but for now we'll put the sites we need directly into
this file. It also enables .php files to be served by the PHP module, and means
that we can access index.php documents with the single /.

Open the following in your text editor:

```
/opt/local/apache2/conf/extra/httpd-vhosts.conf.
```

Read the comments in the file, then delete (or comment out) everything bar the NameVirtualHost line.

Now add the following, being careful to change the /path/to/your/sites/ bit to
wherever you keep your websites (I presume you keep them all in one place, like
    a good little developer):

```
<Directory "/path/to/your/sites/"> Options All AllowOverride All Order allow,deny Allow from all </Directory>
```

Also add the following, for phpMyAdmin:

```
<Directory "/opt/local/www/phpmyadmin/"> Options All AllowOverride All Order allow,deny Allow from all </Directory>
```

These two chunks of config give Apache the right to serve the contents of those directories to the outside world, so if you need more security, you can
configure this as needed.

Add this to your httpd-vhosts.conf file (feel free to change the .local bit to
    anything you prefer):

```
<VirtualHost *:80> ServerName phpmyadmin.local DocumentRoot /opt/local/www/phpmyadmin/ </VirtualHost>
```

Open /etc/hosts in your text editor, and add the following line:

```
127.0.0.1 phpmyadmin.local
```

Save it, and enter your password if prompted.

Now restart Apache:

```sh
apache2ctl restart
```

Note that there's no "sudo" at the beginning. This is important, as the call to
apache2ctl will fail if there's a "sudo" before it (the command it aliases to
    already contains the sudo command).

Now visit <http://phpmyadmin.local> and with any luck you'll be prompted for
your database username (root) and password (which you set earlier). Success!
Have a sandwich.

(I hate glib lines like that when things don't work, so if you have any trouble,
comment me up).

### Python and Django

Now we can install the necessaries for Django. We'll need Python (2.6 is the
    version I favour at the moment), and mod_wsgi. If you're more comfortable
    with mod_python that's fine, but for production environments, WSGI is a much
    better approach, and as we're after mirroring our production environment as
    much as possible, this makes sense. (If you really want mod_python, replace
        the mod_wsgi bit below with mod_python26.)

```sh
sudo port install python26 mod_wsgi py26-mysql
```

Go back to /opt/local/apache2/conf/httpd.conf, find the last LoadModule line and
add the following after it:

```
LoadModule wsgi_module modules/mod_wsgi.so
```

Get Django, along with some useful packages (setuptools and PIL are a must;
ElementTree and BeautifulSoup are good for XML and HTML parsing):

```sh
sudo port install py26-setuptools py26-pil py26-lxml py26-elementtree py26-beautifulsoup py26-markdown py26-django
```

You can of course remove any or all of the above (including Django), and install
the framework from SVN or a .gz download. I just like the fact that the latest
stable version of the framework can be installed and updated really easily, and
I don't have to worry about where it's all going; it just slots nicely into
place.

### Conclusion

I wrote this a while ago and have only got round to publishing it now, so there
may be inaccuracies, missing steps and outdated advice. But if you have any
trouble, please leave me a comment, as it's likely something I've missed that
I'll remember fairly quickly, and can add to the guide for future readers.
