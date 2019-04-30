providers = ["Level3", "Verisign", "Google", "Quad9", "DNS.WATCH",
             "Comodo Secure DNS", "OpenDNS Home", "Norton ConnectSafe",
             "GreenTeamDNS", "SafeDNS", "OpenNIC", "SmartViper", "Dyn",
             "FreeDNS", "Alternate DNS", "Yandex.DNS", "UncensoredDNS",
             "Hurricane Electric", "puntCAT", "Neustar", "Cloudflare",
             "Fourth Estate"]

ips = ["209.244.0.3", "64.6.64.6", "8.8.8.8", "9.9.9.9", "84.200.69.80",
       "8.26.56.26", "208.67.222.222", "199.85.126.10", "81.218.119.11",
       "195.46.39.39", "69.195.152.204", "208.76.50.50", "216.146.35.35",
       "37.235.1.174", "198.101.242.72", "77.88.8.8", "91.239.100.100",
       "74.82.42.42", "109.69.8.51", "156.154.70.1", "1.1.1.1", "45.77.165.194"]


####################################
### Part 1 - Provider Dictionary ###
####################################
DNS_dictionary = {}
# print(len(providers))
# print(len(ips))

# Use a for loop to create a dictionary mapping the provider names to their IPs. expected output: {'Level3': '209.244.0.3', ...}
for dns in range(len(providers)):
       DNS_dictionary[providers[dns]] = ips[dns]

   


print("DNS Dictionary: ")
print(DNS_dictionary)
print("--------")

# # Use the dictionary to print Hurricane Electric's IP
print("Hurricane Electric's IP is: " + str(DNS_dictionary["Hurricane Electric"]))
#print(DNS_dictionary["Hurricane Electric"])
print("--------")
print("--------")


# ##################################
# ### Part 2 - List of Providers ###
# ##################################
sec_dictionaries = {}
proly = []


for a,b in DNS_dictionary.items():
       sec_dictionaries = {}
       sec_dictionaries["provider_name"] = a
       sec_dictionaries["primary_server"] = b
       proly.append(sec_dictionaries)



# # Use a for loop to create a list of dictionaries with the associated information. expected output: [{'provider_name': 'Level3', 'primary_server': '209.244.0.3'}, ...]


print("DNS Dictionaries: ")
#print(proly[0]) used for when you want to get to a specific location inside the list through an index
print(proly)
print("--------")


# # Use the list to print the total number of providers
print("Number of providers: " + str(len(providers)))
print("--------")
print("--------")

#print(len(providers))