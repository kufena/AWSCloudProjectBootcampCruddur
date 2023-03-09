# Week 3 — Decentralized Authentication

## Ugh!

I've played around with Cognito a bit, but not like this.  I guess I'd used the built in UI, and it was some time ago.  I used an identity pool to set some attributes that you could use directly in Service Roles, so, for instance, you could ensure a user only saw their stuff.

Well, I followed along.  I was three or four days behind as I was away, but I have it up to the end of server side verify stuff.  I have more questions than I'd like:

  - is it actually talking to Cognito when it's verifying the token?
  - what's going on with expiry?  I think it really is expiring the token and not using a refresh token to renew it, but is this checked in the front end?

Well, that's two for now.