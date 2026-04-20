import argparse

from ingest import ingest_logs
from detection import run_detection
from ip_check import check_ip
from alerts import get_alerts   






def main():
    parser = argparse.ArgumentParser(description="AlertChain SIEM CLI")

    sub=parser.add_subparsers(dest="command", help="Available commands")

    """
    ingest command
    """
    ingest = sub.add_parser("ingest", help="Ingest data into AlertChain SIEM")
    ingest.add_argument("--source", required=True, help="Source of the data (e.g., file, API)")
    ingest.add_argument("--format", required=True, help="Format of the data (e.g., json, csv)")
    ingest.add_argument("--path", required=True, help="Path to the data file or API endpoint")


    """
    scan    
    """

    scan = sub.add_parser("scan", help="Scan for threats in AlertChain SIEM")
    scan.add_argument("--file", required=True, help="Path to the file to scan")     

    """
    ip check
    """
    ip=sub.add_parser("ip", help="Check if an IP address is malicious")
    ip.add_argument("--check", required=True, help="IP address to check")

    """
    alerts
    """

    sub.add_parser("alerts", help="View recent alerts in AlertChain SIEM")

    args = parser.parse_args()

    if args.command == "ingest":
        ingest_logs(args.source, args.format, args.path)
        print("Data ingested successfully.")
    elif args.command == "scan":
        run_detection(args.file)
        print("File scanned successfully.")
    elif args.command == "ip":
        check_ip(args.check)
    elif args.command == "alerts":
        alerts=get_alerts()
        for alert in alerts:
            print(alert)




if __name__ == "__main__":
    main()




