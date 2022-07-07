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
-- 162: Earlier that morning theif withdrawing money from ATM on Leggett Street.
-- 163: As theif left bakery they called someone and talked for less than a minute. Planned to take the earliest flight out tomorrow. Asked person on phone to purchase flight.

-- Identify license plate #.
SELECT *
FROM bakery_security_logs
WHERE month = 7
AND day = 28;

-- Check ATM record.
SELECT *
FROM atm_transactions
WHERE month = 7
AND day = 28
AND atm_location = 'Leggett Street';
-- Use account_number to find person_id

-- Bank accounts.
SELECT *
FROM bank_accounts
WHERE account_number IN
(SELECT account_number
FROM atm_transactions
WHERE month = 7
AND day = 28
AND atm_location = 'Leggett Street');
-- Use person id.

-- Check phone records.
SELECT *
FROM phone_calls
WHERE month = 7
AND day = 28
AND duration < 60;

-- Check flights.
SELECT *
FROM flights
WHERE month = 7
AND day = 29;
-- Flight id = 36 to airport id 4.

-- Check airport id.
SELECT *
FROM airports
Where id = 4;
-- Distination is NYC.

-- Check passengers.
SELECT *
FROM passengers
WHERE flight_id = 36;

-- Indentify person.
SELECT *
FROM people
WHERE id IN
    (SELECT person_id
    FROM bank_accounts
    WHERE account_number IN
        (SELECT account_number
        FROM atm_transactions
        WHERE month = 7
        AND day = 28
        AND atm_location = 'Leggett Street'))
AND passport_number IN
    (SELECT passport_number
    FROM passengers
    WHERE flight_id = 36)
AND license_plate IN
    (SELECT license_plate
    FROM bakery_security_logs
    WHERE month = 7
    AND day = 28);