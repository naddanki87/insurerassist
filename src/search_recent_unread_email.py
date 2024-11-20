from pathlib import Path
from gmail_api import init_gmail_service, get_latest_unread_email_inbox, download_attachments_message, mark_email_as_read, is_email_spam, get_email_attachments_info
from file_operation import  read_all_files_in_directory, delete_all_files_in_folder
# Create the Gmail API service
client_file = 'token.json'
service = init_gmail_service(client_file)


latest_email = get_latest_unread_email_inbox(service)
msg_id = latest_email['msg_id']
user_id = 'me'
download_dir = Path('./downloads')

# Display email details
if latest_email:
    print(f"Checking if email with subject '{latest_email['subject']}' is spam...")
    is_spam = is_email_spam(service, msg_id)

    if is_spam:
        print("This email is marked as spam no further actions. Need to request or send email saying please mark as NOT A SPAM")
    else:
         print("Latest Unread Email in INBOX:")
         print(f"Subject: {latest_email['subject']}")
         print(f"From: {latest_email['sender']}")
         print(f"Date: {latest_email['date']}")
         print(f"Snippet: {latest_email['snippet']}")
         print(f"Body: {latest_email['body']}")
         attachments = get_email_attachments_info(service, msg_id)

         if attachments:
             print("Attachments found:")
             download_attachments_message(service, msg_id, download_dir)
             for attachment in attachments:
                 print(f"Filename: {attachment['filename']}, Attachment ID: {attachment['attachmentId']}")
         else:
             print("No attachments found.")

         result = mark_email_as_read(service, msg_id)
         content = read_all_files_in_directory(download_dir)

         if content:
                print(content)
         if result:
                print("Email marked as read successfully.")
         else:
                print("Failed to mark the email as read.")

    delete_all_files_in_folder(download_dir)
else:
    print("No unread emails found in INBOX.")



