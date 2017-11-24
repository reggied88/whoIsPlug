from errbot import BotPlugin, botcmd
from subprocess import Popen, PIPE, STDOUT

class WhoIsDomain(BotPlugin):
    """This plugin allows a user to return the whois info of a domain"""
    err_version = '5.1.3'

    def activate(self):
        super(WhoIsDomain, self).activate()

	try:
		Popen(['whois'], stdout=PIPE, stderr=STDOUT).communicate()
	except Exception as e:
		self.warn_admins("This plugin uses whois and it wasn't found on your system") 

    @botcmd
    def whois(self, msg, args):
        return Popen(['whois'] + args.split, stdout=PIPE, STDOUT).communicate()
