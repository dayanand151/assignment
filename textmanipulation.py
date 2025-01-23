import re

class LogProcessor:
    def __init__(self, filename):
        self.filename = filename
        self.logs = []

    def load_logs(self):
        """Reads the log file and loads all lines into memory."""
        with open(self.filename, 'r') as file:
            self.logs = file.readlines()

    def filter_errors(self):
        """Filters only 'ERROR' logs."""
        self.logs = [log for log in self.logs if 'ERROR' in log]

    def convert_to_uppercase(self):
        """Converts the logs to uppercase."""
        self.logs = [log.upper() for log in self.logs]

    def remove_timestamp_and_clean(self):
        """Removes the timestamp and keeps only log level, user, and message."""
        cleaned_logs = []
        for log in self.logs:
            # Use regex to remove the timestamp (first two space-separated words)
            match = re.sub(r'^[^ ]* [^ ]* ', '', log)
            cleaned_logs.append(match)
        self.logs = cleaned_logs

    def sort_logs_by_user(self):
        """Sorts the logs by user alphabetically."""
        # Sort by the user name, which is enclosed in square brackets.
        self.logs.sort(key=lambda log: re.search(r'\[(.*?)\]', log).group(1))

    def get_processed_logs(self):
        """Returns the processed logs."""
        return self.logs


if __name__ == "__main__":
    log_processor = LogProcessor('server.log')
    log_processor.load_logs()  
    log_processor.filter_errors()
    log_processor.convert_to_uppercase()
    log_processor.remove_timestamp_and_clean()
    log_processor.sort_logs_by_user()
    processed_logs = log_processor.get_processed_logs()
    for log in processed_logs:
        print(log)
