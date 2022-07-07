-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Find crime of interest.
SELECT *
FROM crime_scene_reports
WHERE street = 'Humphrey Street'
AND day = 28;
-- Id = 295. Took place at 10:15am. Three interviews conducted.

-- Look at interviews.
SELECT *
FROM interviews
WHERE month = 7
AND day = 28;
-- 161: Left within 10min of theft.
-- 162: 

-- Identify license plate #.
SELECT *
FROM bakery_security_logs
WHERE month = 7
AND day = 28;
-- license plate # is