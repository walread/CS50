-- Keep a log of any SQL queries you execute as you solve the mystery.

-- find crime of interest
SELECT *
FROM crime_scene_reports
WHERE street = 'Humphrey Street'
AND day = 28;
-- id = 295

-- look at interviews
SELECT *
FROM bakery_security_logs
WHERE id = 295;
-- license plate is IH61G08, but day is 29th rather than 28th...