-- this script ranks country origins of bands ordered by fans
-- from metal_bands.sql
SELECT origin, SUM(fans) AS Nb_fans FROM metal_bands
GROUP BY origin
ORDER BY Nb_fans DESC;
