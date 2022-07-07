-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Find crime of interest.
SELECT *
FROM crime_scene_reports
WHERE street = 'Humphrey Street'
AND day = 28;
-- Took place at 10:15am. Three interviews conducted.

-- Look at interviews.
SELECT *
FROM interviews
WHERE month = 7
AND day = 28;
-- 161: Left within 10min of theft.
-- 162: Earlier that morning say theif getting money from ATM on Leggett Street.
-- 163: As theif left bakery they called someone and talked for less than a minute. Planned to take the earliest flight out tomorrow. Asked person on phone to purchase flight.

-- Identify license plate #.
SELECT *
FROM bakery_security_logs
WHERE month = 7
AND day = 28;
-- License plate # is

-- Check ATM record.

-- Check phone records.

-- Check flights.

-- Check credit card purchases.