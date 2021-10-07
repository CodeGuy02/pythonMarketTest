#ui TEST -

def handleButtonLogin(self):
    self.ActivityText.append('Logging In...')

    #call(["python Login.py"])
    self.launch_script()


def handleButtonLogout(self):
    self.ActivityText.append('Logging out...')

    global session
    global logout_state
    print('==================')
    print('Logging out now...')
    print('==================')

    url_logout = url + 'LogOut?source=SOURCEID'
    request = session.get(url_logout)
    print(request.content)
    logout_state = True

def launch_script(self):
        #self.panel = Login.runscript()
        #self.panel.show()
        global session
        print('================')
        print('=    Login     =')
        print('================')

        username = str(raw_input('User Name:'))
        password = str(raw_input('Password: '))
        post_data = {'userid': username, 'password': password, 'source': 'SOURCE_ID', 'version': '1001'}
        print('post_data = ')
        print(post_data)

        session = requests.session()
        request = session.post(url_login, post_data, headers)

        print('request.content = ')
        print(request.content)

        self.BalancesAndPositions()

        self.priceHistory()