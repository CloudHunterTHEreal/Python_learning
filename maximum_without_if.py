"""Get maximum without using  if-else, loops and standard max() function"""
def my_abs(arg):
    """Get absolute value the arg"""
    return (arg ** 2) ** 0.5

numbers = [float(input(f"Input {number_name} number: ")) for number_name in ('first', 'second')]
difference = numbers[0]  - numbers[1]

print('Maximum:', numbers[int(bool((difference) - my_abs(difference)))])
