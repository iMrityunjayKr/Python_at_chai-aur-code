try:
    file = open('example.txt', 'w')  # Open the file in write mode
    file.write('chai aur code')      # Write to the file

finally:
    file.close()                     # Close the file to free resources
