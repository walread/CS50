-- Keep a log of any SQL queries you execute as you solve the mystery.

-- find crime of interest
SELECT *
FROM crime_scene_reports
WHERE street = 'Humphrey Street'
AND day = 28;
-- Id = 295. Took place at 10:15am. Three interviews conducted.

-- Identify license plate #.
SELECT *
FROM bakery_security_logs
WHERE id = 295;
-- license plate # is 

-- Look at interviews.