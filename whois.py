from errbot import BotPlugin, botcmd
from subprocess import Popen, PIPE, STDOUT

class WhoIsDomain(BotPlugin):
    """This plugin allows a user to return the whois info of a domain"""
    err_version = '5.1.3'

    @botcmd
    def whois(self, msg, args):
        """Say whats up to the world"""
        return Popen(['whois'] + args.split, stdout=PIPE, STDOUT)
