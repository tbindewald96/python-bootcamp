def is_leap_year(year):
    """Takes a year as an input and tells if leap year or not."""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else: 
            return True
    elif year % 4 != 0:
        return False
        
        
print(is_leap_year(1989))