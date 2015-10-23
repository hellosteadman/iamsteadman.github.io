Title: Social Comments
Date: 2013-06-24
Category: Projects
Summary: Let users post comments via Twitter, Facebook, LinkedIn or the old-fashioned way, by specifying their name, email address and website
Tags: django

## Setup

1. Install from the Python Package Index:  
`pip install socialcomments`

2. Add `socialcomments` to your `INSTALLED_APPS` list

3. Add the following to your URLconf:  
`url(r'^comments/', include('socialcomments.urls'))`

4. Run `python manage.py syncdb` or `python manage.py migrate`

## Configuration

The `SOCIAL_COMMENTS_PROVIDERS` tuple sets out the various providers that can be
used with Social Comments and their respective settings. Currently this project
supports Twitter, Facebook, LinkedIn and a basic name-email-URL combination. The
`SOCIAL_COMMENTS_PROVIDERS` setting should look something like this:

	SOCIAL_COMMENTS_PROVIDERS = (
		(
			'socialcomments.providers.twitter.TwitterProvider', {
				'CONSUMER_KEY': '<your customer key>',
				'CONSUMER_SECRET': '<your consumer secret>'
			}
		),
		(
			'socialcomments.providers.facebook.FacebookProvider', {
				'CONSUMER_KEY': '<your customer key>',
				'CONSUMER_SECRET': '<your consumer secret>'
			}
		),
		(
			'socialcomments.providers.linkedin.LinkedInProvider', {
				'CONSUMER_KEY': '<your customer key>',
				'CONSUMER_SECRET': '<your consumer secret>'
			}
		)
	)

For Twitter and Facebook you shouldn't need to set a callback URL when creating
your app, but you might need to for LinkedIn. The URL is http://example.com/comments/connect/callback/, where
"example.com" is your domain, and assuming "comments" is the URL stem you've
chosen (you should be able to choose any prefix in your URLconf).

<a class="btn" href="https://github.com/iamsteadman/social-comments">
    <span class="octicon octicon-git-branch"></span>
    Fork it on GitHub
</a>
