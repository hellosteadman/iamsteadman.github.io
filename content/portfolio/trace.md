Title: Trace
Date: 2014-09-02
Tags: django
Category: Portfolio
Summary: A complex assessment and reporting app for the education sector, written in Django

Services for Education commissioned [Substrakt](http://substrakt.com/), my
employer to build a SaaS platform for the education sector, following changes in
legislation.

The curriculum design, assessment and reporting tool allows teachers to create a
sequence of work for pupils and track their progress through the National
Curriculum. Headteachers and auditors can see reports of pupil, cohort and
whole-school progress in realtime.

The site runs Django 1.6 on AWS, using Elastic Beanstalk to provision and deploy
servers in a scalable architecture.

This is one of the most complex projects I've worked on, and has tested my maths
skills to the limit. The reports require complex calculations which have to be
performed quickly. This means a lot of raw SQL as well as parsing data within
Python... and knowing when such jobs should be performed at the database or
business-logic level.

The Python code is written entirely by me, with 99% of the interface built by me
using Twitter Bootstrap, with design and user-interface work provided almost
entirely by Substrakt's Creative Director, Jim Braithwaite.

## Design

<iframe src="https://player.vimeo.com/video/111732346" width="730" height="455" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>

This video shows how sequences of work are designed, by picking statements from
the National Curriculum, and grouping them together, ordering them and providing
notes as teaching aids.

## Assessment

<iframe src="https://player.vimeo.com/video/111762755" width="730" height="455" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>

This video demonstrates the assessment area, where pupils' progress is marked.
Completed assessments can be audited by another person, internal or external to
the school.

## Reporting

<iframe src="https://player.vimeo.com/video/111767419" width="730" height="455" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>

This video shows the reports that can be generated via the system, which queries
data in realtime, via raw SQL queries that have been finely-tuned after months
of iteration.

<a class="btn" href="https://s4etrace.co.uk/" target="_blank">
    <span class="octicon octicon-eye"></span>
    Find out more about Trace
</a>
