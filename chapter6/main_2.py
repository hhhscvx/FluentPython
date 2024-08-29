charles = {'name': 'Charles L. Dodgson', 'bord': 1832}

lewis = charles
print(lewis is charles)

alex = {'name': 'Charles L. Dodgson', 'bord': 1832}  # фейк паспорт

print(alex == charles)
print(alex is not charles)  # думайте
