from pathlib import Path
from gmail_api import init_gmail_service, get_email_message_details, download_attachments_message


# Create the Gmail API service
client_file = 'token.json'
service = init_gmail_service(client_file)
msg_id = '193464ed6f9d25cd'
message = get_email_message_details(service,msg_id)

print(message)

if message:
    print(f"Subject: {message['subject']}")
    print(f"From: {message['sender']}")
    print(f"Recipients: {message['recipients']}")
    print(f"Body: {message['body']}...")  # Print first 100 characters of the body
    print(f"Snippet: {message['snippet']}")
    print(f"Has Attachments: {message['has_attachments']}")
    print(f"Date: {message['date']}")
    print(f"Star: {message['star']}")
    print(f"Label: {message['label']}")

if message['has_attachments']:
    download_dir = Path('./downloads')
    download_attachments_message(service, msg_id, download_dir)