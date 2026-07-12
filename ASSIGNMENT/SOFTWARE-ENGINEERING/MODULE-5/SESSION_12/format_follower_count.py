# Write a function called format_follower_count that takes a number and returns it in Instagram-style format (e.g., 1500 as '1.5K', 1200000 as '1.2M').<br><br><em><strong>Hint:</strong> Use if-elif-else to check the number range and format accordingly.</em>

def format_follower_count(num):
        if num < 1000:
             return str(num)
        elif num < 1000000:
          return str(num / 1000) + "K"
        else:
             return str(num / 1000000) + "M"
                

print(format_follower_count(100))