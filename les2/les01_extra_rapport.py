# les01_extra_rapport.py
# Hoeveel servers?
aantal_servers = int(input("Hoeveel servers wil je controleren? "))

servers = []

# Gegevens verzamelen
for i in range(aantal_servers):
    print()
    print(f"--- SERVER {i + 1} ---")

    servernaam = input("Servernaam: ")
    ip_adres = input("IP-adres: ")
    totaal_ram = float(input("Totaal RAM in GB: "))
    gebruikt_ram = float(input("Gebruikt RAM in GB: "))
    totale_schijf = float(input("Totale schijfruimte in GB: "))
    gebruikte_schijf = float(input("Gebruikte schijfruimte in GB: "))
    besturingssysteem = input("Besturingssysteem: ")
    uptime = float(input("Uptime in dagen: "))

    # Berekeningen
    vrij_ram = totaal_ram - gebruikt_ram
    percentage_ram = (gebruikt_ram / totaal_ram) * 100

    vrije_schijf = totale_schijf - gebruikte_schijf
    percentage_schijf = (gebruikte_schijf / totale_schijf) * 100

    # Status bepalen
    if percentage_ram >= 90 or percentage_schijf >= 90:
        status = "KRITIEK"
    elif percentage_ram >= 70 or percentage_schijf >= 70:
        status = "WAARSCHUWING"
    else:
        status = "OK"

    # Servergegevens opslaan
    server = {
        "naam": servernaam,
        "ip": ip_adres,
        "ram_totaal": totaal_ram,
        "ram_gebruikt": gebruikt_ram,
        "ram_vrij": vrij_ram,
        "ram_percentage": percentage_ram,
        "schijf_totaal": totale_schijf,
        "schijf_gebruikt": gebruikte_schijf,
        "schijf_vrij": vrije_schijf,
        "schijf_percentage": percentage_schijf,
        "os": besturingssysteem,
        "uptime": uptime,
        "status": status
    }

    servers.append(server)


# Gemiddelden berekenen
gemiddeld_ram = sum(server["ram_percentage"] for server in servers) / aantal_servers
gemiddeld_schijf = sum(server["schijf_percentage"] for server in servers) / aantal_servers

# Aantal kritieke servers
aantal_kritiek = sum(
    1 for server in servers if server["status"] == "KRITIEK"
)


# RAPPORT AFDRUKKEN
balk_gelijk = "=" * 55
balk_min = "-" * 55
titel = "SYSTEEMRAPPORT – CVO Vitant Monitoring"

print()
print(balk_gelijk)
print(titel.center(55))
print(balk_gelijk)

# Alle servers tonen
for i, server in enumerate(servers):
    print()
    print(f">> SERVER {i + 1} - SERVER-INFO")
    print(f"   {'Servernaam':<14}: {server['naam']}")
    print(f"   {'IP-adres':<14}: {server['ip']}")
    print(f"   {'OS':<14}: {server['os']}")
    print(f"   {'Uptime':<14}: {server['uptime']:.1f} dagen")
    print(f"   {'Status':<14}: {server['status']}")

    print()
    print("   >> GEHEUGEN (RAM)")
    print(f"      {'Totaal':<10}: {server['ram_totaal']:.1f} GB")
    print(
        f"      {'Gebruikt':<10}: "
        f"{server['ram_gebruikt']:.1f} GB "
        f"({server['ram_percentage']:.1f}%)"
    )
    print(f"      {'Vrij':<10}: {server['ram_vrij']:.1f} GB")

    print()
    print("   >> SCHIJFRUIMTE")
    print(f"      {'Totaal':<10}: {server['schijf_totaal']:.1f} GB")
    print(
        f"      {'Gebruikt':<10}: "
        f"{server['schijf_gebruikt']:.1f} GB "
        f"({server['schijf_percentage']:.1f}%)"
    )
    print(f"      {'Vrij':<10}: {server['schijf_vrij']:.1f} GB")


# SAMENVATTING
print()
print(balk_min)
print(">> SAMENVATTING")
print(f"   {'Servers gecontroleerd':<25}: {aantal_servers}")
print(f"   {'Gemiddeld RAM-gebruik':<25}: {gemiddeld_ram:.1f}%")
print(f"   {'Gemiddeld schijfgebruik':<25}: {gemiddeld_schijf:.1f}%")
print(f"   {'Servers met status KRITIEK':<25}: {aantal_kritiek}")
print(balk_min)

