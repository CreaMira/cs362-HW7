def is_leapYear(years):

    if(years % 4 == 0):
        if (years % 100 == 0):
            return False
        
        return True

    return False