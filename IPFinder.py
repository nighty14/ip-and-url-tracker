# Dev/ED : Pavan Ananth Sharma

import socket
from ip2geotools.databases.noncommercial import DbIpCity



url = input("would you like to know something?:")
url = input("Enter the URL you want to track : ")
ip = socket.gethostbyname(url)
reponse = DbIpCity.get(ip, api_key = 'free')







print("IP: ", ip)
print("City: ",reponse.city)
print("Region: ",reponse.region)
print("Coutry: ",reponse.country)





print("                                        *888b                                                                                                                                                             ")
print("                                         8888                                                                                                                                                             ")
print("                                         8888                                                                                                                                                             ")
print("                                         8888                                                                                                                                                             ")
print("       =====               =========     8888                                                                                                                                                             ")
print("     ==========         =======   ===    8888                                                                                                                                                             ")
print("  =====   ======      =======     ====   8888b                                                                                                                                                            ")
print(" =====      =====    ======              88888888888888b     a888888888888b   ad888ba         ad888ba  ad888ba         ad888ba     ad88888888ba     ad88888b                                              ")
print(" =====       ===========                 888888888888888b              8888b    d8888b       d8888b      d8888b       d8888b     ad88        88ba     888888    ad888888ba                                ")
print("               ========                  8888b      d8888    a88888888888888b     d8888b    8888b          d8888b    8888b       ad88        88ba     888888   88888   888b                               ")
print("                                         8888        8888  d888          *88b       d88888d88888             d88888d88888        ad88        88ba     8888888888888                                       ")
print("                                         8888        8888  d888          a88b      d8888b  d8888b           d8888b  d8888b       ad88        88ba     888888                                              ")
print("                                         8888        8888  d888          a88b     d8888b     d8888b        d8888b     d8888b     ad88        88ba     888888                                              ")
print("                                         8888        8888   d88888888888888b    d88888b       d88888b    d88888b       d88888b    *888888888888*      888888                                              ")
print("                                                                              _________________________________                                                                                           ")
print("                                                                             /                                 \                                                                                          ")
print("                                                                            |    DEVELOPED BY: ~haxx0r d0xK     |                                                                                         ")
print("                                                                            |                                   |                                                                                         ")
print("                                                                            |     EXPECT WHAT THE FAIR IS!      |                                                                                         ")
print("                                                                            |           (ANON MEMBER)           |                                                                                         ")
print("                                                                            |                                   |                                                                                         ")
print("                                                                             \_________________________________/                                                                                          ")   