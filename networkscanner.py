from scapy.all import *

dest_ip = "192.168.1.1/24"
arp = ARP(pdst=dest_ip) #arp packet creation
ether = Ether(dst="ff:ff:ff:ff:ff:ff") #broadcast
packet=ether/arp

result = srp(packet,timeout=3)[0] # sends and receives packets. Set timeout =3 so it doesnt get stuck 

clients=[]

for send, receive in result:
	clients.append({'ip': receive.psrc, 'mac': receive.hwsrc})

print("These are the devices in the network:")
print("IP" + " "*18 +" MAC")

for client in clients:
	print("{:16}      {}".format(client['ip'],client['mac']))
