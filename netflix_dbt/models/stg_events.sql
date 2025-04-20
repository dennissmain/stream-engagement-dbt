SELECT
    timestamp,
    user_id,
    movie_id,
    genre,
    action,
    duration
FROM public.events
WHERE action IS NOT NULL
  AND user_id IS NOT NULL
  AND movie_id IS NOT NULL
  AND genre IS NOT NULL
  AND duration IS NOT NULL
  AND timestamp IS NOT NULL
  