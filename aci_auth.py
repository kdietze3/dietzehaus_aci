#!/Python27/python
#Environment Python 2.7 Windows 10 ACI 2.3(1f)

#Simple module for ACI login and logout

from cobra.mit.access import MoDirectory
from cobra.mit.session import LoginSession

# Suppress HTTPS Warnings
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def aci_login(apic_url, username, password):
    #Create login session and actually login
    loginSession = LoginSession(apic_url, username, password)
    moDir = MoDirectory(loginSession)
    moDir.login()
    return moDir

def aci_logout(moDir):
    #Logout
    moDir.logout()

