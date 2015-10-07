import calendar
import os
import shutil
import sys

from argparse import ArgumentParser

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "-start_year",
        default=2014,
        type=int
    )
    parser.add_argument(
        "-end_year",
        default=2016,
        type=int
    )
    parser.add_argument(
        "-dir",
        required=True
    )
    args = parser.parse_args()

    if os.path.exists(os.path.join(args.dir, str(args.start_year))):
        delete = input("Delete all contents of " + args.dir + "? (True/False) ")
        if not delete:
            print "Destination directory not empty: exiting."
            sys.exit(1)
        else:
            shutil.rmtree(args.dir)
            os.mkdir(args.dir)

    for year in range(args.start_year, args.end_year + 1):
        year = str(year)
        os.mkdir(os.path.join(args.dir, year))
        open(os.path.join(args.dir, year, "log.txt"), "w").close()
        months = ["0" + str(i) for i in range(1, 10)]
        months.extend([str(i) for i in range(10, 13)])
        for month in months:
            os.mkdir(os.path.join(args.dir, year, month))
            open(os.path.join(args.dir, year, month, "log.txt"), "w").close()
            _, days_in_month = calendar.monthrange(int(year), int(month))
            days = ["0" + str(i) for i in range(1, 10)]
            days.extend([str(i) for i in range(10, days_in_month + 1)])
            for day in days:
                os.mkdir(os.path.join(args.dir, year, month, day))
                open(os.path.join(args.dir, year, month, day, "log.txt"), "w").close()
