"""
#fill in the details of the item you plan to buy
item = {
    "Name": ...,
    "Info": ...,
}
#Print the item details in the following format:

Item:
    Name: item name
    Info: item info
"""
items =[ {
    "Name":"Asus",
    "Info": "black laptop 14'",
    "Price": 65_999.00
}, {
    "Name":"Secrid",
    "Info":"Metallic black wallet from Rijks Museum",
    "Price": 5_000.00
},{
    "Name":"Avocadoria",
    "Info":"Avocado shake with tapioca balls",
    "Price": 185.00

}]
for item in items:
    for key,values in item.items():
        print(f"\t {key}: {values}")











