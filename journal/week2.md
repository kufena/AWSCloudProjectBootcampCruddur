# Week 2 — Distributed Tracing

## Adding Honeycomb tracing.

Went ok - at first it didn't work but you have to 

```
docker compose up --build
```

in order to get it to create a new image.  If you have added requirements or npm libraries, or environment variables, you need to do the build.  I didn't do that to begin with, and so it failed to find opentelemetry.

I tried to get it to add the console logging, but that failed to install or init the processors.  I will need to retry that.

Another thing I noticed - if you use the POST part of the front end, it doesn't appear to log the content - ie the text you reply with.  I wasn't sure if you could see it - you can filter on fields in the span, but http.content, http.body wasn't there.

## Adding honeycomb tracing to the browser?

I've started on this by adding some bits to the package.json, and creating a ```tracing.js``` file with some bits from the documentation.
Inside the HomeFeedPage.js page I imported the tracer javascript and it creates and Active Span and adds an attribute, before ending.
I think the idea is to do the loadData part inside the span, so that we get some timing data, but it doesn't do that at the minute.

What I can't see is where the KEY goes that gets passed to Honeycomb?  There's no way of identifying me.  It needs more work.

After that, how to send the trace data to the backend and continue the trace inside the backend.
