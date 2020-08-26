#!/usr/local/bin/python3.7

import calendar
# Show every month
for month in range(1, 13):
    cal = calendar.monthcalendar(2020, month)
    first_week  = cal[0]
    second_week = cal[1]
    third_week  = cal[2]

    # If a Saturday presents in the first week, the second Saturday
    # is in the second week.  Otherwise, the second Saturday must
    # be in the third week.

    if first_week[calendar.TUESDAY]:
        holi_day = second_week[calendar.TUESDAY]
    else:
        holi_day = third_week[calendar.TUESDAY]

    print('%3s: %2s' % (calendar.month_abbr[month], holi_day))
