import urllib2, sys, time
import base64
import getpass

DEBUG_ENABLED = True
RELOGIN_INTERVAL = 5	#seconds
URL = 'https://chilli4.snac.unimelb.edu.au:4990/www/login.chi'
FILE = 'login.info'

def get_password():
    return getpass.getpass()

def encode_password(pw):
    return base64.b64encode(pw)

def decode_password(encoded):
    return base64.b64decode(encoded)

class LoginInfo():
    def __init__(self, id):
        self.file = FILE
        self.id = id
        self.pw = None
        self.is_save = (id == None)

    def start(self):
        if self.id == None:
            #Load file
            if self.load() == False:
                self.input_info()
        else:
            self.input_pw()

    def input_id(self):
        self.id = raw_input("ID:")
    def input_pw(self):
        self.pw = get_password()
    def input_save(self):
        is_save = raw_input("Want to save? (y/n)")
        if is_save == "Y" or is_save == "y":
            self.is_save = True
        else:
            self.is_save = False

    def input_info(self):
        self.input_id()
        self.input_pw()
        self.input_save()
        if self.is_save:
            self.save()

    def save(self):
        f = open(self.file, 'w')
        f.write(encode_password(self.id.strip())+'\n')
        f.write(encode_password(self.pw.strip())+'\n')
        f.close()

    def load(self):
        try:
            f = open(self.file, 'r')
            self.id = decode_password(f.readline().strip())
            self.pw = decode_password(f.readline().strip())
            f.close()
            return True
        except IOError:
            return False
    def get_id(self):
        return self.id

    def get_pw(self):
        return self.pw


class AutoLoginer():
    def __init__(self, debug=False):
        self.id = None
        self.pw = None
        self.debug = debug
        self.login_url = URL

    def is_logged_in(self):
        response = urllib2.urlopen(self.login_url)
        html = response.read()
        is_logged = '<form name="form" method="post"' not in html
        if self.debug: print "Is logged in? ", is_logged
        return is_logged

    def get_login_redirect_url(self):
        login_url = "%s?username=%s&password=%s"%(self.login_url, self.id, self.pw)
        response = urllib2.urlopen(login_url)
        html = response.read()
        html2 = html[html.find("url=")+4:]
        redirect_url = html2[:html2.find('"/>')]
        if self.debug: print "Redirect URL: ", redirect_url

        return redirect_url

    def login_newman(self, redirect_url):
        response = urllib2.urlopen(redirect_url)
        html = response.read()
        return '<h2>Success!</h2>' in html

    def login(self):
        login_success = False

        if self.pw != None:
            redirect_url = self.get_login_redirect_url()
            login_success = self.login_newman(redirect_url)

        if self.debug: print "Login Success? ", login_success
        return login_success

    def start(self, id, pw):
        self.id = id
        self.pw = pw
        try:
            login_counter = 0
            while True:
                if self.is_logged_in():
                    login_counter +=1
                else:
                    print "NOT LOGGED IN! Try to login again!"
                    login_counter = -1
                    for i in range(3):
                        if self.login():
                            login_counter = 1
                            break
                        print "Login Failed. Attempts: %d / 3" %(i+1)
                    if login_counter == -1:
                        print "Cannot login. Check the ID and password."
                        return True
                if self.debug: print "login counter: %d, and sleep for %d seconds" % (login_counter, RELOGIN_INTERVAL)
                time.sleep(RELOGIN_INTERVAL)
        except urllib2.URLError:
            print "Error: not in Newman network. Run the program again"
            return False
            
def main(argv):
    id = pw = None
    debug = DEBUG_ENABLED

    if len(argv) > 1: id = argv[1]
    login_info = LoginInfo(id)
    login_info.start()

    loginer = AutoLoginer(debug)
    while loginer.start(login_info.get_id(), login_info.get_pw()):
        login_info.input_info()

if __name__ == "__main__":
    main(sys.argv)

