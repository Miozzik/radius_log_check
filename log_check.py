from sys import argv
import re
def check_log(fille, lines=5):
    with open(fille, encoding="utf-8") as log_file:
        log_file = log_file.readlines()
        for check_line in log_file[-int(lines)*2::2]:
            log_time = re.search(r"<Timestamp.*>(.+)</Timestamp>", check_line).group(1)
            user_name = re.search(r"<User-Name.*>(.+)</User-Name>", check_line).group(1)
            client_ip =  re.search(r"<Client-IP-Address.*>(.+)</Client-IP-Address>", check_line).group(1)
            client_name = re.search(r"<Client-Friendly-Name.*>(.+)</Client-Friendly-Name>", check_line).group(1)
            print(f"Подключился {user_name} с устройства {client_name} и ip: {client_ip} в {log_time}")

check_log(argv[1], argv[2])