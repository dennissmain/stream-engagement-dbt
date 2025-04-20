-- models/user_genre_engagement.sql

WITH watched AS (
    SELECT *
    FROM {{ ref('stg_events') }}
    WHERE action = 'watch'
),

likes AS (
    SELECT user_id, genre, COUNT(*) AS like_count
    FROM {{ ref('stg_events') }}
    WHERE action = 'like'
    GROUP BY user_id, genre
)

SELECT
    w.user_id,
    w.genre,
    COUNT(DISTINCT w.movie_id) AS unique_movies_watched,
    COUNT(*) AS total_watch_events,
    SUM(w.duration) AS total_watch_time,
    AVG(w.duration) AS avg_watch_duration,
    COALESCE(l.like_count, 0) AS likes_in_genre
FROM watched w
LEFT JOIN likes l
  ON w.user_id = l.user_id AND w.genre = l.genre
GROUP BY w.user_id, w.genre, l.like_count