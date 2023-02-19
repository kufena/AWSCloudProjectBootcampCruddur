# Week 1 — App Containerization

## Following week 1 live stream.

Managed to follow the live stream quite easily, as I had a little bit of experience with docker.  However, the experts were a real bonus here, and they explained a few things that were really cool, like following the docker files back to scratch, the distinction between host and guest OS and more pertinently, the difference between the container and the guest OS.  The container is just the layered file system, an image is just the files that create this layered fs and some things required by it, and this all runs on a guest os when the container is run.

Also, the difference between RUN and CMD - RUN happens during the build phase, CMD is run when the container is started.

The whole thing was quite cool.  I shall run locally at some point.  Also study docker compose a bit more as that seems a bit more magicky.

## Adding the backend notifications endpoint.

This went ok, but I had some problems with Type Errors when I tried to run just the back end container.  But this went away when I did

'''
docker compose up
'''

## Adding the fronend notifications page.

So, I did all that Andrew did in the video, and if I go directly to /notifications I see what I guess I should see.
But somewhere the navigation on the left has cocked up and I see something a bit weird, and I'm not quite sure how to fix it.

## Running DynamoDB locally.

I have been doing this for sometime.  It's really easy to do, although i have always run it as an endpoint (seperate container) and never in the docker compose context, which I guess would be more useful?  

