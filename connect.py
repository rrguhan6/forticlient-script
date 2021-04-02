import pexpect

username = ''
password = ''
server_url = ''


child = pexpect.spawn('/opt/forticlient-sslvpn/64bit/forticlientsslvpn_cli  --server ' +
                      server_url+' --vpnuser '+username+'  --keepalive')

child.sendline(password+'\r')

# enter
child.sendline('y\r')
child.interact()
