#!/usr/bin/env python3
import shutil
import psutil
import socket
import os
import sys
import emails

def check_reboot():
    """Return True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")

def check_no_network():
    """Returns True if it fails to resolve google's URL, false otherwise"""
    try:
        socket.gethostbyname("localhost")
        return False
    except:
        return True

def check_root_full():
    """Returns True if the root partition is full,False otherwise."""
    return check_disk_full(disk="/",min_gb=2, min_percent=10)

def check_disk_full(disk, min_gb, min_percent):
    """Returns True if there isn't enough disk space, False otherwise. """
    du = shutil.disk_usage(disk)
    #Calculate the percentage of free space
    percent_free = 100 * du.free /du.total
    #Calculate how many free gigabytes
    gigabytes_free =  du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_gb:
        return True
    return False

def check_cpu():
    cpu = psutil.cpu_percent()
    treshhold = 80.0
    if cpu >= treshhold:
        return False

def check_memory():
    mem =  psutil.virtual_memory()
    treshhold = 500 *1024 * 1024  # 500MB
    if mem.available <= treshhold:
        return False
    #rint(mem.available /(2**30 ))


def main():
    checks=[
        (check_cpu,"Error - CPU usage is over 80%"),
        (check_reboot, "Pending Reboot"),
        (check_memory, "Error - Available memory is less than 500MB"),
        (check_root_full, "Error - Available disk space is less than 20%"),
        (check_no_network, "Error - localhost cannot be resolved to 127.0.0.1")
    ]
    everything_ok = True
    for check, msg in checks:
        if check():
            print(msg)
            everything_ok = False

    if not everything_ok:
        sys.exit(1)

    print("Everything ok.")
    sys.exit(0)
    user = os.environ.get('USER')
    #paragraph = get_data()
    today = datetime.date.today().strftime("%B %d, %Y")
    #title = "Processed Update on {}".format(today)
    #attachment = "/tmp/processed.pdf"
    reports.generate_report(attachment, title, paragraph)
    email = emails.generate_email("automation@example.com", user + "@example.com",
                                  "Upload Completed - Online Fruit Store",
                                  "All fruits are uploaded to our website successfully. A detailed list is attached to this email.",
                                  attachment)
    emails.send_email(email)


main()