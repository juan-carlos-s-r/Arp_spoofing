import subprocess

def get_arp_table():
    result = subprocess.run(['arp', '-a'], capture_output=True, text=True)
    return result.stdout

def save_arp_table(reference_file='arp_reference.txt'):
    arp_table = get_arp_table()
    with open(reference_file, 'w') as file:
        file.write(arp_table)
    print("Tabla ARP guardada como referencia.")

def compare_arp_tables(reference_file='arp_reference.txt'):
    current_arp_table = get_arp_table()
    with open(reference_file, 'r') as file:
        reference_arp_table = file.read()

    if current_arp_table == reference_arp_table:
        print("La tabla ARP no ha sido modificada.")
    else:
        print("¡Advertencia! La tabla ARP ha sido modificada.")
        print("Tabla ARP actual:\n", current_arp_table)
        print("Tabla ARP de referencia:\n", reference_arp_table)

# Guardar la tabla ARP actual como referencia
save_arp_table()

# Comparar la tabla ARP actual con la de referencia
compare_arp_tables()

