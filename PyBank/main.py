import csv
import os



# Initialize variables
total_months = 0
net_total = 0
prev_profit_loss = None    
changes = []
dates = []

greatest_increase = {"date": "", "amount": float('-inf')}
greatest_decrease = {"date": "", "amount": float('inf')}

# Open the CSV file and read the data
with open('Module3Challenge/python-challenge/PyBank/Resources/budget_data.csv','r') as file:
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
    
 # Prepare the analysis text
analysis_text = f"Financial Analysis\n----------------------------\n"
analysis_text += f"Total Months: {total_months}\n"
analysis_text += f"Total: ${net_total}\n"
analysis_text += f"Average Change: ${average_change:.2f}\n"
analysis_text += f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n"
analysis_text += f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n"

# Print the analysis to the terminal
print(analysis_text)

# Export the analysis to a text file
output_path = 'Module3Challenge/python-challenge/PyBank/analysis'
with open('Module3Challenge/python-challenge/PyBank/analysis/financial_analysis.txt', 'w') as output_file:
        output_file.write(analysis_text)

print(f"Analysis has been exported to {output_path}")
