# IS601 Module 12 — Assignment Reflection

**GitHub Repository:** https://github.com/alb641/IS601-MOD12

## Overview

Module 12 focused on extending the FastAPI Calculator application by integrating JWT authentication with calculation BREAD operations. Building on the database functionality from previous modules, I worked on connecting user authentication to PostgreSQL so that each user could securely manage their own calculation records.

This assignment helped me better understand how authentication, authorization, database persistence, and API endpoints work together in a backend application.

## Implementation and Testing

I implemented user registration and login endpoints, JWT-based authentication, and protected calculation endpoints using FastAPI dependencies. The calculation functionality supports Browse, Read, Edit, Add, and Delete operations, allowing users to manage their saved calculations.

An important part of the implementation was connecting each calculation to its owner through a user ID. This allowed the application to filter records by the authenticated user rather than allowing unrestricted access to the database.

I also used Pydantic schemas for request validation, SQLAlchemy for database interactions, and pytest for automated testing. After troubleshooting the remaining issues, my final local test run resulted in **94 passing tests, 1 skipped test, and 0 failures**.

## Challenges Encountered

One challenge I faced was getting JWT authentication to work properly in Swagger. I made changes so I could enter my login token and test the endpoints, but those changes caused five of my existing tests to fail. I had to update the code again so both Swagger and the tests would work.

I also forgot that my test database was still named `module11_test_db` from the previous module. This caused 29 errors because the database didn't exist in my current PostgreSQL container. Once I created it, most of the errors disappeared.

Lastly, I kept getting 404 errors in Swagger because I was using the example calculation ID instead of an actual database record. This taught me to pay closer attention to API responses when testing endpoints.

## Reflection

This module helped me better understand how authentication works beyond just logging in. I learned how to protect user information and make sure users can only access their own records.

I already know to pay attention to error codes and normally I would be overwhelmed by a bunch of failed errors but I'm glad this time I noticed it was just missing database. 

Overall, Module 12 helped me become more comfortable with JWT authentication, database operations, and troubleshooting. Moving forward, I want to be more careful with my database setup and check my configurations earlier to avoid unnecessary errors.

**GitHub Repository:** https://github.com/alb641/IS601-MOD12
