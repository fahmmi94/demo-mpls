#Storing details of all network devices
devices = {
    'R1': {
        'device_type': 'cisco_ios', # Device type for Netmiko connection
        'host': '192.168.223.111', # Device IP address
        'username': 'admin', # SSH username
        'password': 'cisco', # SSH password
        'port': '22', # SSH port
        'secret': 'cisco', # Enable secret (privilege mode password)
    },
    'R2': {
        'device_type': 'cisco_ios',
        'host': '192.168.223.112',
        'username': 'admin',
        'password': 'cisco',
        'port': '22',
        'secret': 'cisco',
    },
    'R3': {
        'device_type': 'cisco_ios',
        'host': '192.168.223.113',
        'username': 'admin',
        'password': 'cisco',
        'port': '22',
        'secret': 'cisco',
    },
    'R4': {
        'device_type': 'cisco_ios',
        'host': '192.168.223.114',
        'username': 'admin',
        'password': 'cisco',
        'port': '22',
        'secret': 'cisco',
    },
    'PE-1': {
        'device_type': 'cisco_ios',
        'host': '192.168.223.115',
        'username': 'admin',
        'password': 'cisco',
        'port': '22',
        'secret': 'cisco',
    },
    'PE-2': {
        'device_type': 'cisco_ios',
        'host': '192.168.223.116',
        'username': 'admin',
        'password': 'cisco',
        'port': '22',
        'secret': 'cisco',
    },
    
}