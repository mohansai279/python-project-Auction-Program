# silent_auction.py

import os

auction_items = {
    "Wine Basket": {"value": 150, "starting_bid": 50, "highest_bid": 0, "highest_bidder": None},
    "Dinner for Two": {"value": 100, "starting_bid": 40, "highest_bid": 0, "highest_bidder": None},
    "Handmade Quilt": {"value": 300, "starting_bid": 100, "highest_bid": 0, "highest_bidder": None}
}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_items():
    print("\nAvailable Auction Items:")
    for idx, (item, info) in enumerate(auction_items.items(), 1):
        print(f"{idx}. {item} (Value: ${info['value']}, Starting Bid: ${info['starting_bid']})")

def place_bid():
    display_items()
    item_name = input("\nEnter the exact name of the item you want to bid on: ").strip()
    if item_name not in auction_items:
        print("Item not found.")
        return
    bidder = input("Enter your name: ")
    try:
        bid = float(input("Enter your bid amount: $"))
    except ValueError:
        print("Invalid bid amount.")
        return

    item = auction_items[item_name]
    min_bid = max(item["starting_bid"], item["highest_bid"] + 1)
    if bid >= min_bid:
        item["highest_bid"] = bid
        item["highest_bidder"] = bidder
        print(f"Bid accepted. {bidder} is now the highest bidder on '{item_name}' with ${bid}.")
    else:
        print(f"Bid too low. Minimum acceptable bid is ${min_bid}.")

def show_results():
    print("\n🧾 Auction Results:")
    for item, info in auction_items.items():
        if info["highest_bidder"]:
            print(f"{item} won by {info['highest_bidder']} with a bid of ${info['highest_bid']}.")
        else:
            print(f"{item} received no bids.")

def main():
    print("🎉 Welcome to the Silent Auction System 🎉")
    while True:
        print("\nChoose an option:")
        print("1. Place a bid")
        print("2. View auction results")
        print("3. Exit")
        choice = input("Enter choice (1-3): ").strip()

        if choice == '1':
            place_bid()
        elif choice == '2':
            show_results()
        elif choice == '3':
            print("Thank you for participating!")
            break
        else:
            print("Invalid choice. Try again.")

        input("\nPress Enter to continue...")
        clear()

if __name__ == "__main__":
    main()
