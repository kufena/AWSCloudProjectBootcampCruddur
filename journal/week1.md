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

## Adding dynamodb and postgres to the docker compose.

Yep that seemed to work ok, although I'm not entirely sure still what all the docker compose bits do.  I guess that's some work for while I'm away at the Norfolk Developers conference.

## Running the whole thing locally.

This did NOT go so well, largely because I am not sure what is going on with flask and react and all that.
For a start, it didn't like *FLASK_ENV* and kept saying it was deprecated?  Also, the compose file itself builds some environment variables - *FRONTEND_URL* and *BACKEND_URL* using some gitpod specific environment variables.  Once I'd worked that out, it was easy to modify those to just use localhost and the respective pots and it ran ok.

I am still getting a problem with the navigation in the front end, though.  Two screenshots here, showing the home and notifications pages which I can get to by URL, but not through the navigation links, which aren't showing.

<p><img src="./Screenshot 2023-02-21 194511.png"/>
<p><img src="./Screenshot 2023-02-21 194541.png"/>


