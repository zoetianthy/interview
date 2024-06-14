It’s a couple of weeks after joining your new team and you've been tasked with
analyzing some background jobs for compute time used. The jobs are taking longer
than expected, so your task is to determine the **total cost** of the most
expensive job.

Your team’s senior engineer explained that the jobs by themselves usually don’t
take very long to complete, but each job can spawn between 1–15 other jobs,
which can themselves spawn more jobs. They explain that the total cost for a job
is the sum of how long the job took plus the time all of the jobs it spawned
took.

They sketch out a quick example illustrating their point:

```
         A: 5ms
          / \
         /   \
    B: 1ms   C: 3ms
```

The **total cost** for `A` is `5 + 1 + 3`, or `9ms`.

They also mention that the top-level jobs like `A` do not have a `parent_id`
set, and that the jobs are stored in execution order - meaning spawned jobs
occur after the spawning job in the file.

Feeling that you’ve got a handle for the problem, they share the `jobs.json` file
with you and ask you to send them the total cost of the longest job within the
hour. Oddly enough, they also mention that the third-longest job took `8967ms` to
run…

Each `id` only occurs once in the file, although it may appear many times as a
`parent_id`.

Please respond with the **total cost for the longest job** in `jobs.json`.