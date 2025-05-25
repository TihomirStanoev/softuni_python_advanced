reservations = int(input())

tickets = []

while True:
    command = input()
    if command == 'END':
        break
    tickets.append(command)


party_tickets = set(tickets[:reservations]) - (set(tickets[reservations:]))

print(len(party_tickets))
print('\n'.join(ticket for ticket in sorted(party_tickets)))