# Exemple de script pour configurer un réseau VPN avec OpenVPN

import os

def setup_vpn():
    os.system('sudo apt-get install openvpn -y')
    os.system('sudo openvpn --config /etc/openvpn/my_vpn_config.ovpn')

if __name__ == "__main__":
    setup_vpn()
    print("VPN configuré avec succès.")
