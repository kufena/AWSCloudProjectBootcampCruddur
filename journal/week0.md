# Week 0 — Billing and Architecture

## Gitpod, AWS, GitHub

Installed the aws cli on gitpod and configured it.
If you do what you're used to and use 'aws configure' then it'll put the credentials in '~/.aws/credentials'.
To use the environment variables, you need to remove this file, if it's there.

Also, gp env BLAH="xxxxx" isn't enough - you still need to do the export BLAH="xxxxx" - or so it was for me.