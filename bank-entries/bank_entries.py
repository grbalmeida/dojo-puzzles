# -*- coding: utf-8 -*-

import re
import datetime

def bank_entries(check_in):
    regex_is_valid_check_in = '^\[\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}\:\d{2}\]\s-\sAbertura\sda\sPorta\sOK$'
    is_valid_check_in = not re.search(regex_is_valid_check_in, check_in) == None
    is_valid_entry_time = False

    if is_valid_check_in:
        year = int(check_in[1:5])
        month = int(check_in[6:8])
        day = int(check_in[9:11])
        hours = int(check_in[12:14])
        minutes = int(check_in[15:17])
        seconds = int(check_in[18:20])

        try:
            date = datetime.datetime(year, month, day, hours, minutes, seconds)
            is_valid_entry_time = hours >= 10 and hours <= 16
        except:
            is_valid_check_in = False
            is_valid_entry_time = False

    responses = {
        'is_valid_check_in': is_valid_check_in,
        'is_valid_entry_time': is_valid_check_in and is_valid_entry_time
    }

    return responses