from helpers.logger import logger


class EmailService:

    def send_verification_email(self, email, uu_id):
        logger.info(f'Sending email to {email} with message {uu_id}')
