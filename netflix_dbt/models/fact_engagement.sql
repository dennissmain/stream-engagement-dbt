SELECT
    movie_id,
    genre,
    COUNT(*) FILTER (WHERE action = 'watch') AS watch_count,
    COUNT(*) FILTER (WHERE action = 'like') AS like_count,
    SUM(duration) FILTER (WHERE action = 'watch') AS total_watch_time
FROM {{ ref('stg_events') }}
GROUP BY movie_id, genre