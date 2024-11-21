from pathlib import Path
from gmail_api import init_gmail_service, get_latest_unread_email_inbox,mark_email_as_read, is_email_spam,get_attachments_as_dict,encode_to_base64
from file_operation import delete_all_files_in_folder

import json
# Create the Gmail API service
client_file = 'token.json'
service = init_gmail_service(client_file)


latest_email = get_latest_unread_email_inbox(service)

user_id = 'me'
download_dir = Path('./downloads')

if latest_email:
    msg_id = latest_email['msg_id']
    print(f"Checking if email with subject '{latest_email['subject']}' is spam...")
    is_spam = is_email_spam(service, msg_id)

    if is_spam:
        print("This email is marked as spam. No further actions. Request the sender to mark as NOT SPAM.")
    else:
        print("Processing latest unread email in INBOX:")
        print(f"Subject: {latest_email['subject']}")
        print(f"From: {latest_email['sender']}")
        print(f"Date: {latest_email['date']}")
        print(f"Snippet: {latest_email['snippet']}")
        print(f"Email Body: {latest_email['body']}")

        email_body_base64 = encode_to_base64(latest_email['body'])
        attachments_base64 = get_attachments_as_dict(service, msg_id)

        # Prepare the final JSON structure
        final_json = {
            "email_body": email_body_base64,
            "attachments": attachments_base64 if attachments_base64 else {}
        }

        truncated_attachments = {key: value[:100] for key, value in final_json["attachments"].items()}
        final_json_preview = {
            "email_body": email_body_base64[:100],  # Truncate the email body for preview
            "attachments": truncated_attachments
        }

        print("Final JSON Preview:")
        print(json.dumps(final_json_preview, indent=4))

        # Mark email as read
        result = mark_email_as_read(service, msg_id)
        if result:
            print("Email marked as read successfully.")
        else:
            print("Failed to mark the email as read.")

    # Clean up downloaded files
    delete_all_files_in_folder(download_dir)
else:
    print("No unread emails found in INBOX.")



