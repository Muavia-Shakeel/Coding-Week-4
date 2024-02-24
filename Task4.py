class AuctionItem:
    def __init__ (self, item_number, description, reserve_price):
        self.item_number = item_number
        self.description = description
        self.reserve_price = reserve_price
        self.number_of_bids = 0
        self.highest_bid = 0
        self.highest_bidder = None
        
    def place_bid(self, bid_amount, buyer_number):
        if bid_amount > self.highest_bid:
            self.highest_bid = bid_amount
            self.highest_bidder = buyer_number
            self.number_of_bids += 1
            return True
        return False

def add_auction_items():
        items = []
        item_numbers = set()
        for i in range(2): # Ensuring at least 10 items
            while True:
                item_number = input("Enter item number: ")
                if item_number in item_numbers:
                    print("Error: Item number must be unique. Please try again.")
                    continue
                description = input("Enter item description: ")
                if not description:
                    print("Error: Description cannot be empty. Please try again.")
                    continue
                reserve_price = input("Enter reserve price: ")
                try:
                    reserve_price = float(reserve_price)
                    if reserve_price <= 0:
                        raise ValueError
                except ValueError:
                    print("Error: Reserve price must be a positive number. Please try again")
                    continue
                
                items.append(AuctionItem(item_number, description, reserve_price))
                item_numbers.add(item_number)
                break
        
        return items
    
def place_bid_on_item(auction_items):
    item_number = input("Enter item number to bid on: ")
    item = next((item for item in auction_items if item.item_number == item_number), None)

    if item is None:
        print("Item not found.")
        return 
    print(f"Item Number: {item.item_number}, Description: {item.description}, Current Highest Bid: {item.highest_bid}")    
    buyer_number = input("enter your buyer number: ")
    bid_amount = float(input("Enter your bid amount: "))
    if item.place_bid(bid_amount, buyer_number):
        print("Bid placed successfully. ")
    else:
        print("Bid must be higher than the current highest bid.")
        
        
def process_auction_results(auction_items):
    total_fee = 0
    items_sold = 0  # Initialize counter for sold items
    items_below_reserve = []
    items_no_bids = []

    for item in auction_items:
        if item.number_of_bids > 0:
            if item.highest_bid >= item.reserve_price:
                items_sold += 1  # Increment the sold items counter
                fee = item.highest_bid * 0.1
                total_fee += fee
            else:
                items_below_reserve.append((item.item_number, item.highest_bid))
        else:
            items_no_bids.append(item.item_number)

    # Display the results
    print(f"Total auction company fee from sold items: ${total_fee:.2f}")
    print(f"Items sold: {items_sold}")
    print(f"Items below reserve price: {len(items_below_reserve)}")
    print(f"Items with no bids: {len(items_no_bids)}")

    if items_below_reserve:
        print("\nItems that did not meet the reserve price:")
        for item_num, bid in items_below_reserve:
            print(f"Item Number: {item_num}, Final Bid: {bid}")

    if items_no_bids:
        print("\nItems with no bids:")
        for item_num in items_no_bids:
            print(f"Item Number: {item_num}")


                
        
def main():
    print("Auction Setup")
    auction_items = add_auction_items()
    while True:
        action = input("Do you want to place a bid? (yes/no): ")
        if action.lower() == "yes":
            place_bid_on_item(auction_items)
        else:
            break
    
    process_auction_results(auction_items)

if __name__ == "__main__":
    main()

        