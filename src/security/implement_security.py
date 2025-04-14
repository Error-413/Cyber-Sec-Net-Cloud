import os

def configure_firewall():
    # Commande pour configurer un pare-feu sur Linux
    os.system('sudo ufw enable')
    os.system('sudo ufw allow ssh')
    os.system('sudo ufw allow http')
    os.system('sudo ufw allow https')
    os.system('sudo ufw default deny incoming')
    os.system('sudo ufw default allow outgoing')

if __name__ == "__main__":
    configure_firewall()
    print("Pare-feu configuré avec succès.")
