import csv

with open("ledger.csv", 'r') as file:
    csvreader = csv.reader(file)
    fields = next(csvreader)
    down = []
    up = []
    for row in csvreader:
        if not any(row):
            break
        if float(row[3]) < 0:
            down.append(row)
        elif float(row[3]) > 0:
            up.append(row)

    # Determine net amount owed by each player
    net = {}
    zelle = {}
    exc_zelle = {}
    for player in up + down:
        net[player[0]] = float(player[3])
        zelle[player[0]] = float(player[6])
        exc_zelle[player[0]] = float(player[7])
    # determine players with non-zero net balance
    players = []
    for player in net:
        if net[player] != 0:
            players.append(player)          
            
    # create dictionary to store transaction amounts
    transactions = {payer: {recipient: 0 for recipient in players} for payer in players}
    max_player_flags = {player: 0 for player in players}
    possible_pairs = {}
    
    for key1 in net:
        values = []
        for key2 in net:
            if key1 != key2:
                values.append(key2)
        possible_pairs[key1] = values
    # calculate transaction amounts to minimize cash flow
    not_possible_dict = {}
    while True:
        max_net = 0
        for key in possible_pairs:
            if net[key] > max_net:
                max_player = key
                max_net = net[key]
        min_net = 10000000
        for value in possible_pairs[max_player]:
            if net[value] < min_net:
                min_player = value
                min_net = net[value]
                
        if (exc_zelle[max_player] and not zelle[min_player]) or (exc_zelle[min_player] and not zelle[max_player]):
        # if the transaction is not possible, skip to the next iteration
            not_possible_dict[max_player] = min_player
            possible_pairs[max_player].remove(min_player)
            possible_pairs[min_player].remove(max_player)
            continue
        # break if all players have zero net balance
        if net[max_player] == 0 and net[min_player] == 0:
            break
        # calculate transaction amount
        amount = min(abs(net[max_player]), abs(net[min_player]))
        # update net balances
        net[max_player] -= amount
        net[min_player] += amount
        # update transaction dictionary
        transactions[max_player][min_player] += amount

    # Write payment instructions to script
    with open("payments.txt", "w") as outfile:
        for recipient in transactions:
            for payer, amount in transactions[recipient].items():
                if amount > 0:
                    outfile.write(f"{payer} owes {recipient} ${amount:.2f}\n")