import time

from database import fetch_data
from monitor import ChangeMonitor
from chart import LiveChart

from config import POLL_INTERVAL


def main():

    print("Starting SQL Monitor...")

    monitor = ChangeMonitor()
    chart = LiveChart()

    while True:

        try:

            df = fetch_data()

            monitor.detect_changes(df)

            chart.update(df)

            time.sleep(POLL_INTERVAL)

        except KeyboardInterrupt:

            print("\nStopped.")

            break

        except Exception as e:

            print("ERROR:", e)

            time.sleep(POLL_INTERVAL)


if __name__ == "__main__":
    main()