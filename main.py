import smtplib
from email.message import EmailMessage

sender_email = input("\nEnter Your ( sender ) Email : ")
sender_email_pass = input("Enter Your GMAIL Password : ")

recievers_email = []

while True:
    reciever_email = input("\nEnter Reciever Email : ")
    recievers_email.append(reciever_email)
    
    add_another = input("\nDo You Wanna Add Another Reciever ? ( y / n ) : ")
    
    if add_another.lower() == "n":
        print("\nRecievers Email Added ......")
        break
    elif add_another.lower() != "y":
        print("\nPlease Enter 'n' or 'y' accordingly")

sub = input("\nEnter Subject : ")
body = ""
print("\nEnter Body : ")

while True:
    line = input("Enter 'done' When Message Completed : ")
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
    for receiver in recievers_email:
        em = EmailMessage()
        em['From'] = sender_email
        em['To'] = receiver
        em['Subject'] = sub
        em.set_content(body)

        # Send the email
        server.sendmail(sender_email, receiver, em.as_string())

        print("Email sent successfully to " + receiver)

print("\nEmails Sent To All Receivers")
