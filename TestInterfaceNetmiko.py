from netmiko import ConnectHandler

print("********Antes de lanzar los comandos de configuración:*********")
device = ConnectHandler(device_type='cisco_ios', ip='192.168.0.33',
                        username='cisco', password='cisco')
output = device.send_command("show running-config interface GigabitEthernet 0/0")
print(output)

configcmds = ["interface GigabitEthernet 0/0", "description hola pepa"]
device.send_config_set(configcmds)
print("******Después de mandar los comandos queda la confugiración así*******")
output1 = device.send_command("show running-config interface GigabitEthernet 0/0")

print(output1)
print("******Estado de interfaces*******")
output2 = device.send_command("show int desc")

print(output2)
device.disconnect()
