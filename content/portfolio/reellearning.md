Title: ReelLearning
Date: 2013-09-15
Tags: django
Category: Portfolio
Summary: A video catalogue, CMS and sharing platform written in Django

ReelLearning is a video training project for primary school teachers,
built by me at [Substrakt](http://substrakt.com/) in Django, using Bootstrap.

Originally a Drupal website, I was asked to rebuild it, first running on a
Rackspace Red Hat server, then in 2014 we moved it to Amazon Web Services, using
Elastic Beanstalk.

Schools sign up to ReelLearning to provide training for their teachers. While
the app doesn't handle the payment side, it does manage all of the account
creation, trial signups and user-created content. The catalogue is managed via
the Django admin, using the Grappelli skin. Videos uploaded via the site are
passed to Amazon S3 and served via CloudFront.

## Browse, search and view

<iframe src="https://player.vimeo.com/video/114352311" width="730" height="455" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>

This video shows how users can browse the video catalogue and search it (via
the Haystack Django app).

## Playlists

<iframe src="https://player.vimeo.com/video/114352310" width="730" height="455" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>

This video demonstrates how playlists are created and managed. They can be
shared with other members of a school, and also created by ReelLearning staff
and shared amongst all of the schools using the platform.

## Groups

<iframe src="https://player.vimeo.com/video/114965612" width="730" height="455" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>

This video shows how users create and manage groups. These can be used to group
other users together, such as teachers in a specific year or subject.

<a class="btn" href="http://reellearning.co.uk/" target="_blank">
    <span class="octicon octicon-eye"></span>
    Find out more about ReelLearning
</a>
