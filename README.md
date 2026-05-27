# Minimal Flask License Verification Server

A lightweight HTTP authentication backend built with Python and Flask to validate software license keys.

## Usage

Use this project however you want. You are free to copy the source code and integrate it into your own systems for key verification. The application is ready for deployment on platforms like Render or similar hosting providers.

## IMPORTANT NOTICE!

If you choose to implement this code, ensure you understand the following technical requirements and constraints:

* **Key Management:** All authorized license keys must be stored strictly within the `LICENSE_KEYS` environment variable on your hosting provider (e.g., inside the Environment Variables settings on Render). Keys must be separated by commas. The backend parses this string dynamically on each incoming request.
* **User-Agent Filtering:** This code strictly blocks all incoming requests and denies access to anyone whose `User-Agent` header does not match the specific value defined in the source. Any mismatch immediately triggers an `HTTP 403 Forbidden` response.
* **User-Agent Header:** To pass authentication, your client application must explicitly send the exact `User-Agent` string assigned to the `UsAg` variable in the code. The server will reject any connection attempts that lack this specific identifier.

## API Specification

* **URL:** `/check`
* **Method:** `GET`
* **URL Params:** `key=[key_string]`

### Expected Responses:
* `200 OK` with body `"VALID"` — The key exists in the parsed environment list.
* `200 OK` with body `"INVALID"` — The key is missing or incorrect.
* `403 Forbidden` — Missing or incorrect `User-Agent` header.

## License

This project is licensed under the MIT License. Anyone is free to reuse, modify, or distribute this software without restriction.
