def dict_of_numbers():

    words = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
        10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
        15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"
    }
    tens = {
        20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
        60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"
    }
    result = {}

    for i in range(100):
        if i < 20:
            result[i] = words[i]
        else:
            tens_part = (i // 10) * 10
            unit_part = i % 10
            
            if unit_part == 0:
                result[i] = tens[tens_part]
            else:
                result[i] = f"{tens[tens_part]}-{words[unit_part]}"
                
    return result
