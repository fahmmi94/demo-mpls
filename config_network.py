# configure_network.py

# Import necessary libraries and configurations
from netmiko import ConnectHandler
from devices import devices
from interface_config import interface_configs
from ospf_config import ospf_configs
from bgp_config import bgp_configs
from mpls_config import mpls_configs

# Define the console configuration commands
console_commands = [
    "line console 0",
    "password Maheer",
    "login",
    "exit"
]

# Function to configure a device
def configure_device(device, config_sets):
    try:
        # Connect to the device
        connection = ConnectHandler(**device)
        
        # Enter enable mode
        connection.enable()

        # Apply each set of configurations
        for config_set in config_sets:
            if config_set:
                output = connection.send_config_set(config_set)
                print(f'Configuration Output for {device["host"]}:')
                print(output)
        
        # Disconnect from the device
        connection.disconnect()

    # Handle any exceptions during configuration
    except Exception as e:
        print(f'Failed to configure {device["host"]}: {e}')

# Main function to iterate over all devices and apply configurations
def main():
    for router_name, device in devices.items():
        print(f'Configuring {router_name} ({device["host"]})...')
        # Gather config sets for each device
        config_sets = [
            interface_configs.get(router_name),
            ospf_configs.get(router_name),
            bgp_configs.get(router_name),
            mpls_configs.get(router_name),
        ]
        
        # Configure the device
        configure_device(device, config_sets)

# Start the configuration process
if __name__ == "__main__":
    main()
