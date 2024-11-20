from pathlib import Path
from gmail_api import init_gmail_service, download_attachments_message, download_attachments_thread

client_file = 'token.json'
service = init_gmail_service(client_file)

user_id = 'me'
msg_id = '19348004b0882c2d'
download_dir = Path('./downloads')

download_attachments_message(service,msg_id, download_dir)
# download_attachments_all(service, user_id, msg_id, download_dir)
