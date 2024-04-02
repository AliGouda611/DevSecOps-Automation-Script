import subprocess
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging

def lint_code():
    subprocess.run(["flake8", "example_code.py"], check=True)

def run_unit_tests():
    subprocess.run(["pytest", "tests"], check=True)

def run_static_analysis():
    subprocess.run(["bandit", "-r", "."], check=True)

def run_dependency_scanning():
    subprocess.run(["safety", "check", "--full-report"], check=True)

def run_container_scanning():
    subprocess.run(["trivy", "your_docker_image"], check=True)

def send_notification(subject, body):
    sender_email = "your.email@example.com"
    receiver_email = "recipient.email@example.com"
    smtp_server = "smtp.example.com"
    smtp_port = 587
    smtp_username = "your_smtp_username"
    smtp_password = "your_smtp_password"

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        logging.info("Notification email sent successfully.")
    except Exception as e:
        logging.error("Failed to send notification email:", str(e))

def setup_logging():
    logging.basicConfig(filename='devsecops.log', level=logging.INFO)

def main():
    setup_logging()
    logging.info("DevSecOps pipeline started.")

    lint_code()
    run_unit_tests()
    run_static_analysis()
    run_dependency_scanning()
    run_container_scanning()

    # Check if any security issues were found
    # Replace with actual checks based on tool output
    if True:  # Example condition: if security issues found
        send_notification("Security Issues Found", "One or more security issues were found during the pipeline execution. Please review and address them.")

    logging.info("DevSecOps pipeline completed.")

if __name__ == "__main__":
    main()
