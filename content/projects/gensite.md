Title: Django data provisioner
Date: 2014-07-14
Tags: django, ansible
Category: Projects

I need to do a bunch of frontend development for a site I'm working on, and I
needed a simple way to generate sample data that is sane.

So, inspired by [Ansible](http://ansible.com/) I knocked up a data provisioning
system as a Django management command, that takes a YAML file defining the data
I want to generate.

It can take data from a JSON resource, likt the Random User API, and turn that
into User objects with Profile objects attached, to carry things like the
profile image, gender, date-of-birth and so on.

It needn't be used to generate users; that's just the first thing I needed it to
do. It's intelligently nested, so if you need to create a foreign key
relationship, you just nest the two model statements and the management command
figures out the relationship.

The same goes for linking models via many-to-many relationships, but in reverse.
Here you specify the fieldname you want, and tell the provisioner how many items
you want to use, and whether you want to pick the items starting at a row
number, or just choose them at random. You can also filter and exclude which
items are taken from the database.

It automatically detects file fields and downloads remote images or picks files
from the filesystem. It does this intelligently, as it knows which model you're referencing, so looks in that app's directory to find the relevant file.

<a class="btn" href="https://github.com/iamsteadman/bambu-gensite">
    <span class="octicon octicon-git-branch"></span>
    Fork it on GitHub
</a>
