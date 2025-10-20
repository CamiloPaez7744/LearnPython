def greet(name):
    return f"Hello, {name}!"

print(greet("Angus Young"))

def calculate_price_concert(ticket_price, num_tickets, tax_rate=0.07):
    subtotal = ticket_price * num_tickets
    tax = subtotal * tax_rate
    total = subtotal + tax
    return total

print(calculate_price_concert(100, 2))