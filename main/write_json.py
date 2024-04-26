import pandas as pd

# Sample data
data = {
    'ClaimNumber': ['A12345', 'B67890', 'C13579', 'D24680', 'E13579', 'F24680', 'G13579', 'H24680', 'I13579', 'J24680',
                    'R12345', 'F67890', 'A13579', 'X24680', 'L13579', 'Z24680', 'Y13579', 'X24680', 'D13579', 'A24680',
                    'T12345', 'Y67890', 'B3579', 'Z24680'],
    'ClaimType': ['motor', 'motor', 'home', 'home', 'home', 'motor', 'motor', 'home', 'motor', 'home',
                   '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    'Description': [
        "I've submitted all the required documents for my claim; why hasn't it been processed yet?",
        "I had a minor fender bender, but the garage says the whole car needs to be replaced.",
        "My policy clearly covers water damage, so I don’t understand why my claim was denied.",
        "The adjuster hasn’t returned any of my calls for the past two weeks.",
        "Every time I call, I get a different person and have to explain my situation from scratch.",
        "I've been paying premiums for years, and the one time I need to make a claim, there's an issue.",
        "The amount you've offered to settle my claim is nowhere near enough to cover my losses.",
        "I lost my receipt, but I remember the stolen items were worth thousands.",
        "I reported my car stolen yesterday; it had a lot of expensive upgrades that should be covered.",
        "It's been three months since I filed my claim, and I still haven't received any payment.",
        "I've submitted all the required documents for my claim; why hasn't it been processed yet?",
        "My policy clearly covers water damage, so I don’t understand why my claim was denied.",
        "The adjuster hasn’t returned any of my calls for the past two weeks.",
        "Every time I call, I get a different person and have to explain my situation from scratch.",
        "I've been paying premiums for years, and the one time I need to make a claim, there's an issue.",
        "The amount you've offered to settle my claim is nowhere near enough to cover my losses.",
        "I lost my receipt, but I remember the stolen items were worth thousands.",
        "I reported my car stolen yesterday; it had a lot of expensive upgrades that should be covered.",
        "It's been three months since I filed my claim, and I still haven't received any payment.",
        "I submitted a claim for storm damage to my roof, but now you're saying the damage was pre-existing?",
        "I reported a theft of my designer bags from my car, though I can't provide the original purchase receipts.",
        "I claimed for a medical emergency while traveling, yet the insurer questions the urgency of the treatment.",
        "My home was burglarized and several items were taken, including some very expensive jewelry that was a family heirloom.",
        "The claim for my phone being damaged is legitimate; I don’t see why proof of purchase is necessary since it was a gift.",
        
    ]
}


try:
    df = pd.DataFrame(data)
except ValueError as e:
    print("\nCustom Error: All arrays must be of the same length.")
    for key in data:
        print(f"Length of array under key '{key}': {len(data[key])}")
    print("\n")
    raise ValueError("Data arrays have inconsistent lengths.")


df.to_json('claims_data.json', orient='records')

print("JSON file has been created with the specified data.")
