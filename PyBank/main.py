import csv
import os

# Verify the current working directory and the file path
current_directory = os.getcwd()
file_path = os.path.join(current_directory, 'Resources', 'budget_data.csv')

if not os.path.isfile(file_path):
    print(f"File not found: {file_path}")
else:
    # Initialize variables
    total_months = 0
    net_total = 0
    prev_profit_loss = None
    changes = []
    dates = []

    greatest_increase = {"date": "", "amount": float('-inf')}
    greatest_decrease = {"date": "", "amount": float('inf')}

    # Open the CSV file and read the data
    with open('Resources/budget_data.csv','r') as file:
        reader = csv.DictReader(file)
    
        for row in reader:
            # Extract the date and profit/loss value
            date = row['Date']
            profit_loss = int(row['Profit/Losses'])
        
            # Update the total number of months and net total
            total_months += 1
            net_total += profit_loss
        
            # Calculate the change in profit/losses
            if prev_profit_loss is not None:
                change = profit_loss - prev_profit_loss
                changes.append(change)
                dates.append(date)
            
                # Check for greatest increase
                if change > greatest_increase["amount"]:
                    greatest_increase["amount"] = change
                    greatest_increase["date"] = date
            
                # Check for greatest decrease
                if change < greatest_decrease["amount"]:
                    greatest_decrease["amount"] = change
                    greatest_decrease["date"] = date
        
            # Update the previous profit/loss value
            prev_profit_loss = profit_loss

    # Calculate the average change in profit/losses
    average_change = sum(changes) / len(changes) if changes else 0

    # Print the analysis
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
    print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")
