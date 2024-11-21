sequenceDiagram
    participant U as User
    participant P as Python Script
    participant G as Gmail API
    participant M as Email Metadata
    participant S as Spam Check
    participant B as Email Body
    participant A as Attachments
    participant F as File Operations

    U->>P: Trigger Email Process
    P->>G: Initialize Gmail API Service
    G->>P: Return Gmail Service
    P->>G: Fetch Latest Unread Email
    G->>M: Retrieve Email Metadata
    M->>P: Return Email Metadata
    P->>S: Check if Email is Spam
    S->>P: Return Spam Status
    alt If Email is Not Spam
        P->>B: Extract Email Body
        B->>P: Return Base64 Email Body
        P->>A: Retrieve Attachments
        A->>P: Return Base64 Attachments
        P->>F: Delete Downloaded Files
        F->>P: Confirm Files Deleted
    else
        P->>U: Email Marked as Spam
    end
    P->>G: Mark Email as Read
    G->>P: Confirm Email Marked as Read
    P->>U: Process Complete
