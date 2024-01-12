import smtplib
from email.message import EmailMessage

# Collect sender's email and password
sender_email = input("\nEnter Your (Sender) Email: ")
sender_email_pass = input("Enter Your App Password: ")

# Collect receivers' emails
receivers_email = []
while True:
    receiver_email = input("\nEnter Receiver Email: ")
    receivers_email.append(receiver_email)
    
    add_another = input("\nDo You Want to Add Another Receiver? (y/n): ")
    
    if add_another.lower() == "n":
        print("\nReceivers' Emails Added...")
        break
    elif add_another.lower() != "y":
        print("\nPlease Enter 'n' or 'y' accordingly")

# Collect email subject and body
subject = input("\nEnter Subject: ")
body = ""
print("\nEnter Body (Type 'done' on a new line when the message is completed): ")

while True:
    line = input("Enter Message Line: ")
    if line.strip().lower() == 'done':
        break
    body += line + '\n'

# Establish a connection to the SMTP server outside the loop
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    # Start TLS for security
    server.starttls()

    # Login to the email account
    server.login(sender_email, sender_email_pass)

    # Loop through each receiver and send the email
    for receiver in receivers_email:
        email_message = EmailMessage()
        email_message['From'] = sender_email
        email_message['To'] = receiver
        email_message['Subject'] = subject
        email_message.set_content(body)

        try:
            # Send the email
            server.sendmail(sender_email, receiver, email_message.as_string())

            print(f"\nEmail sent successfully to {receiver}")
        except Exception as e:
            print(f"\nError sending email to {receiver}: {e}")

print("\nEmails Sent To All Receivers")
