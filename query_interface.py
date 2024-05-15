import json
import glob
import argparse
from datetime import datetime

def parse_log(log):
    try:
        return json.loads(log)
    except json.JSONDecodeError:
        return None

def search_logs(level=None, log_string=None, start_time=None, end_time=None, source=None):
    log_files = glob.glob('*.log')
    results = []

    for log_file in log_files:
        with open(log_file, 'r') as file:
            for line in file:
                log_entry = parse_log(line.strip())
                if not log_entry:
                    continue
                
                if level and log_entry["level"] != level:
                    continue
                if log_string and log_string not in log_entry["log_string"]:
                    continue
                if source and log_entry["metadata"]["source"] != source:
                    continue
                if start_time or end_time:
                    log_time = datetime.fromisoformat(log_entry["timestamp"][:-1])
                    if start_time and log_time < start_time:
                        continue
                    if end_time and log_time > end_time:
                        continue

                results.append(log_entry)
    return results

def parse_args():
    parser = argparse.ArgumentParser(description="Search logs.")
    parser.add_argument('--level', type=str, help="Log level to filter by")
    parser.add_argument('--log_string', type=str, help="Log string to search for")
    parser.add_argument('--start_time', type=str, help="Start timestamp in ISO format")
    parser.add_argument('--end_time', type=str, help="End timestamp in ISO format")
    parser.add_argument('--source', type=str, help="Log source file to filter by")
    return parser.parse_args()

def main():
    args = parse_args()
    start_time = datetime.fromisoformat(args.start_time) if args.start_time else None
    end_time = datetime.fromisoformat(args.end_time) if args.end_time else None

    results = search_logs(
        level=args.level,
        log_string=args.log_string,
        start_time=start_time,
        end_time=end_time,
        source=args.source
    )

    for result in results:
        print(json.dumps(result, indent=4))

if __name__ == "__main__":
    main()
