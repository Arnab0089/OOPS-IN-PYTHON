class EmailService:
    def _connect(self):
        print(f'Connecting to email server...')
    
    def _authenticate(self):
        print(f'Authenticating...')
    
    def send_email(self):
        self._connect()
        self._authenticate()
        print(f'Email sent successfully.')
        self._disconnect()

    def _disconnect(self):
        print(f'Disconnecting...')


email=EmailService()
email.send_email()
    