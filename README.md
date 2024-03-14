# Email to CRM Ticket Converter

This Python script automates the conversion of email requests from the Business team into tickets in the CRM system based on the opportunity ID provided in the email.

## Features

- Automatically extracts the opportunity ID from the email subject line.
- Creates a new ticket in the CRM system with the email content and opportunity ID.
- Updates the ticket status based on the email thread.

## Requirements

- Python 3.x
- `imaplib` and `email` modules for handling emails.
- `requests` module for interacting with the CRM system API.

## Installation

1. Clone this repository:
   ```shell
   git clone https://github.com/your-repo/email-to-crm-ticket-converter.git
   pip install imaplib email requests
   python email_to_ticket_converter.py
  ```
2.Install the required dependencies:
   ```shell
   pip install imaplib email requests
  ```

##Configuration
-Set up your email account to allow IMAP access.
-Configure the script with your email server settings and CRM API details.
-Update the script with the necessary mappings for email subject patterns and CRM ticket statuses.
