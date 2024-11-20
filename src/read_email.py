from gmail_api import init_gmail_service, get_email_messages, get_email_message_details

# Create the Gmail API service
client_file = 'token.json'
service = init_gmail_service(client_file)

# Fetch recent messages
messages = get_email_messages(service, max_results=1)

print(messages)
# Print details of each message
for msg in messages:
    details = get_email_message_details(service, msg['id'])
    if details:
        print(f"Subject: {details['subject']}")
        print(f"From: {details['sender']}")
        print(f"Recipients: {details['recipients']}")
        print(f"Body: {details['body']}...")  # Print first 100 characters of the body
        print(f"Snippet: {details['snippet']}")
        print(f"Has Attachments: {details['has_attachments']}")
        print(f"Date: {details['date']}")
        print(f"Star: {details['star']}")
        print(f"Label: {details['label']}")
        print("-" * 50)