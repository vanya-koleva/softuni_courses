# Authentication and Authorization

## What Do They Mean?

-   **Authorization** is the process of verifying what permissions we have as users.
-   **Authentication** is the process of verifying who we are (e.g., logging into an account).

## Types of Credentials

-   **Username and password** – Single-factor authentication
-   **Phone number with sent password/code** – Multi-factor authentication

## Authentication in Django

-   `django.contrib.auth`

    -   An additional package, similar to the admin module.

    -   Provides **permissions**, **groups**, and **users**.

    -   **Cookie-Based User Session Handling**:

        -   Upon login, Django creates a session key and stores it in a cookie.

        -   The session key is stored in the `django_session` table on the backend.

        -   On each request, the cookie is sent and compared using the session middleware to identify the sender.

        -   `SESSION_COOKIE_HTTPONLY = True` – Allows session key to be sent only over HTTPS.

        -   `CSRF_COOKIE_HTTPONLY = True` – Prevents the browser from accessing the cookie via `document.cookie`.

-   `AuthMiddleware` retrieves the user.

-   Works together with `django.contrib.contenttypes`.

## Django Permissions

-   A table with permissions is maintained.

-   Every time a new model is created, new permissions are added.

-   These represent permissions for **CRUD** operations.

## Web Security

### SQL Injection

-   SQL injection is an attack where a malicious user inputs harmful SQL code into data input fields (such as login forms) to manipulate or extract data from the database. This vulnerability occurs when the application does not properly validate or sanitize user input.

### Cross-Site Scripting (XSS)

-   XSS is an attack where a malicious user injects harmful scripts (usually JavaScript) into a website, which then executes in the browsers of other users. This can lead to cookie theft, content manipulation, or redirection to malicious sites.

### URL/HTTP Parameter Tampering

-   In this type of attack, the attacker manipulates the URL or HTTP request parameters to gain unauthorized access to resources or change the application's behavior. For example, changing a product price parameter in the URL to purchase something at a lower cost.

### Cross-Site Request Forgery (CSRF)

-   CSRF forces a logged-in user to perform unintended actions (like submitting a form or making a payment) without their knowledge. This is achieved by sending a specially crafted link or form to the user.

### Brute Force and DDoS Attacks

-   **Brute Force**: An attacker tries many combinations of passwords or keys until the correct one is found.

-   **DDoS (Distributed Denial of Service)**: Overwhelms a website or service with a massive number of requests, causing slowdowns or outages.

### Insufficient Access Control

-   A vulnerability where users or systems gain access to resources or functions without proper authorization. This can lead to data leaks or unauthorized actions.

### Lack of SSL (HTTPS) / Man-in-the-Middle (MITM) Attacks

-   Without SSL (HTTPS), communication between user and website is unprotected. An attacker can intercept, modify, or steal data (like passwords or personal info). MITM attacks occur when an attacker positions themselves between communicating parties and secretly observes or alters the communication.

### Phishing / Social Engineering

-   These are techniques where the attacker deceives the user into revealing sensitive information (like passwords or credit card numbers) or taking certain actions (like installing malware), by pretending to be a trusted person or organization.

