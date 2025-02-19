import argparse
import logging
import sys
from collections import defaultdict
from typing import List, Dict
from kubernetes import client, config

logging.basicConfig(level=logging.INFO)
import time

v1 = None

def get_ip_networks() -> List[str]:
    """Collect IP networks from all the pods in the cluster (Containers have same IP as pods)"""

    global v1  # Use the global v1 object

    if v1 is None:  # Check if v1 has been initialized
        try:
            config.load_incluster_config()
            v1 = client.CoreV1Api()
        except Exception as e:
            logging.error(f"Error: Unable to load Kubernetes configuration: {e}")
            return None
    try:
        pods = v1.list_pod_for_all_namespaces()
        ips = []

        # Print pod names and IPs
        for pod in pods.items:
            logging.info(f"Pod Name: {pod.metadata.name}, IP: {pod.status.pod_ip}")
            if pod.status.pod_ip!=None:
                ips.append(pod.status.pod_ip)


        # Write IPs to a file
        with open("pod_ips.txt", "w") as f:
            for ip in ips:
                f.write(ip + "\n")
        return ips
    except Exception as e:  # Catch any exception
        logging.error(f"Error: Unable to collect IP networks: {e}")
        return []


def check_collisions(file_path: str):
    """Checks the IP addresses in the file and prints all IPs that occur more than once."""
    try:
        with open(file_path, "r") as f:
            ips = f.readlines()

        # Remove newlines and count occurrences
        ip_counts = {}
        for ip in ips:
            ip = ip.strip()
            if ip in ip_counts:
                ip_counts[ip] += 1
            else:
                ip_counts[ip] = 1

        # Print duplicate IPs
        collide_ips = [ip for ip, count in ip_counts.items() if count > 1]
        if collide_ips:
            logging.info("Colliding IPs: %s", collide_ips) 
        else:
            logging.info("No duplicate IPs found.")
    except FileNotFoundError:
        logging.error(f"Error: File not found: {file_path}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    logging.info("Starting IP Collision Checker")
    parser = argparse.ArgumentParser(description="Collect IP address and check for collisions.")
    parser.add_argument("--check-collision", metavar="FILE", help="Path to the file containing IP addresses to check for collisions")
    args = parser.parse_args()
    while True: 
        get_ip_networks()
        if args.check_collision:
            check_collisions(args.check_collision)
        time.sleep(120) # Fetches ip networks every 2 minutes - also we can use watcher from k8s (K8s Watch API), to skip this part, and as soon as pods are created this script should monitor that