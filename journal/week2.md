# Week 2 — Distributed Tracing

## Adding Honeycomb tracing.

Went ok - at first it didn't work but you have to 

```
docker compose up --build
```

in order to get it to create a new image.  If you have added requirements or npm libraries, or environment variables, you need to do the build.  I didn't do that to begin with, and so it failed to find opentelemetry.

I tried to get it to add the console logging, but that failed to install or init the processors.  I will need to retry that.
