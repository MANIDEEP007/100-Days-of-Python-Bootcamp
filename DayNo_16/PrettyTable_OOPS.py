from prettytable import PrettyTable

#Creating PrettyTable object from PrettyTable class
table = PrettyTable()

"""
Using add_column method to construct table of pokemons & its types
add_column params ==> Field Name, List of data for that column
"""
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])

#Using the attributes for PrettyTable object - changing alignment to left from center
table.align = "l"

#Display the table
print(table)
