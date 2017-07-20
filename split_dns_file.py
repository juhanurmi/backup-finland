import sys

if sys.version_info < (3,0,0):
    sys.stderr.write("You need python 3.x or later to run this script\n")
    exit(1)

#import ipaddress

#def valid_ip(ip_string):
#    try:
#        ipaddress.ip_address(ip_string)
#        return True
#    except ValueError:
#        return False

def create_new_line(line, fi_ips_list):
    # Skip some lines and return valid line
    # Too long line to be a normal domain address
    if len(line) > 50:
        return ""
    # Format must be haku.ahmia.fi 188.117.30.83
    if line.count(" ") != 1:
        return ""
    # Create and save new line
    domain, ip_str = line.split(" ")
    ip_str = ip_str.replace('\n', '')
    # Skip too short or long "ip addresses"
    ip_str_len = len(ip_str)
    if ip_str_len < 7 or ip_str_len > 15:
        return ""
    # Validate the IP address
    #if not valid_ip(ip_str):
    #    return ""
    if not ip_str in fi_ips_list:
        return ""
    # Return valid new line
    return ip_str + " " + domain + "\n"

def ProcessLargeTextFile(input_file, output_file, fi_ips_list):
    bunchsize = 1000000     # Experiment with different sizes
    bunch = []
    line_number = 0
    write_times = 0
    with open(input_file, "r") as r, open(output_file, "w") as w:
        for line in r:
            line_number = line_number + 1
            if line_number % bunchsize == 0:
                print("Read %d lines" % line_number)
            # Valid line to save
            new_line = create_new_line(line, fi_ips_list)
            if new_line:
                bunch.append(new_line)
            else:
                continue
            if len(bunch) == bunchsize:
                write_times = write_times + 1
                w.writelines(bunch)
                bunch = []
                print("Wrote %d times" % write_times)
        w.writelines(bunch)

def main():
    with open("2017-07-18_fi_every_ip.txt") as file:
        fi_ips_list = [line.replace('\n', '') for line in file]
    fi_ips_list = []
    ProcessLargeTextFile("20170714_dns.txt", "20170714_fi_dns.txt", fi_ips_list)

if __name__ == '__main__':
    main()
