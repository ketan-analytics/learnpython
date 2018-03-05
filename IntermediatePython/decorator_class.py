class logit(object):
    def __init__(self, logfile='output1.txt'):
        self.logfile = logfile

    def __call__(self, func):
        log_string = "Function:" + func.__name__ + " was called."
        print(log_string)

        with open(self.logfile, 'a') as opened_file:
            opened_file.write(log_string + '\n')

        self.notify()

    def notify(self):
        pass

class email_logit(logit):
    '''
    A logit implementation for sending emails to admins
    when the function is called.
    '''
    def __init__(self, email='ketannp@hotmail.com', *args, **kwargs):
        self.email = email
        super(email_logit, self).__init__(*args, **kwargs)

    def notify(self):
        # Send an email to self.email
        # Will not be implemented here
        pass



@logit()
def myfunc():
    pass


@logit(logfile='outoupt2.txt')
def myfunc():
    pass



@logit(logfile='outoupt2.txt')
def myfunc1():
    pass