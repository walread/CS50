-- Keep a log of any SQL queries you execute as you solve the mystery.

SELECT *
FROM crime_scene_reports
WHERE street = 'Humphrey Street'
AND day = 28;
-- crime of interest is id 295

SELECT *
FROM bakery_security_logs
WHERE id = 295;
-- license plate is IH61G08, but day is 29th rather than 28th... 