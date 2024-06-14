import pandas as pd

# data = [
#     {"Query": "What is covered under Section 1: Liability?", 
#      "Response": "Section 1: Liability covers injury to third parties or "
#                  "damage caused to their property, not to the car being driven."},
    
#     {"Query": "Am I covered if my car is damaged?", 
#      "Response": "If your car is damaged, we’ll pay the cost of repairing "
#                  "or replacing your car up to its UK market value at the "
#                  "time of the claim."},
    
#     {"Query": "Can I drive my car abroad?", 
#      "Response": "If you want to use your car abroad, your cover depends "
#                  "on the type of policy you have and where you’re driving. "
#                  "Full details can be found in 'Where you can drive' on "
#                  "page 31."},
    
#     # Add more data here...
# ]



data = [
    {"Query": "What is covered under Section 1: Liability?", 
     "Response": "Section 1: Liability covers injury to third parties or damage caused to their property, not to the car being driven."},
    
    {"Query": "Am I covered if my car is damaged?", 
     "Response": "If your car is damaged, we’ll pay the cost of repairing or replacing your car up to its UK market value at the time of the claim."},
    
    {"Query": "Can I drive my car abroad?", 
     "Response": "If you want to use your car abroad, your cover depends on the type of policy you have and where you’re driving. Full details can be found in 'Where you can drive' on page 31."},
    
    {"Query": "What should I do if I need to make a claim?", 
     "Response": "Call 0345 878 6261 to start your claim. Have your personal details, policy number, car registration number, and a description of the loss or damage ready."},
    
    {"Query": "What is not included in my cover?", 
     "Response": "We don’t cover mechanical or electrical failure, wear and tear, damage to tyres caused by braking, punctures, cuts or bursts, and breakdowns. Full details are in 'Losses we don’t cover' on page 33."},
    
    {"Query": "How do I find out who is covered to drive other cars?", 
     "Response": "Your certificate of motor insurance will show who has cover to drive other cars."},
    
    {"Query": "What is DriveSure?", 
     "Response": "DriveSure is our telematics insurance product designed to capture how, when, and where your car is driven, using driver-monitoring technology to base your premium on your driving record."},
    
    {"Query": "Are electric car charging cables covered?", 
     "Response": "Yes, your home charger and charging cables are covered under 'Section 2: Fire and theft' or 'Section 4: Accidental damage'."},
    
    {"Query": "What happens if my car is written off?", 
     "Response": "If your car is written off and we agree to settle your claim, we will have met our responsibilities under the policy. We will not refund any premium if you pay annually."},
    
    {"Query": "How long is the guarantee for repairs carried out by approved repairers?",
     "Response": "Repairs carried out by our approved repairers are guaranteed for five years unless you sell your car or end your lease."},
    
    {"Query": "What should I do if my car is stolen?",
     "Response": "If your car is stolen from a private locked garage, we won’t charge an excess."},
    
    {"Query": "What is the market value of my car?",
     "Response": "The market value is the cost of replacing your car with another of the same make, model, age, mileage, and condition at the time of the accident or loss."},
    
    {"Query": "What are the excess amounts for windscreen repairs?", 
     "Response": "The excess amounts for windscreen repairs and replacement are shown on your car insurance details."},
    
    {"Query": "Can I use my car for business purposes?", 
     "Response": "Business use provides cover for driving in connection with a business or employment. Your certificate of motor insurance will show if your policy includes business use."},
    
    {"Query": "What should I do if I get a communication from a court?",
     "Response": "Contact us straight away if you get any communication such as a notice or form from a court or any threat of legal action."},
    
    {"Query": "What is a courtesy car?", "Response": "A courtesy car is a small hatchback or similar car that an approved repairer supplies to you temporarily on our behalf."},
    
    {"Query": "Are my personal belongings covered in the car?", 
     "Response": "Personal belongings may be covered under 'Section 6: Personal benefits' of the policy."},
    
    {"Query": "How can I contact the motor legal helpline?", 
     "Response": "Call 0345 246 2408 if you have Motor Legal Cover."},
    
    {"Query": "What is the policy period?",
     "Response": "The period of insurance is the length of time you have cover under this policy. It is shown on your certificate of motor insurance and car insurance details."},
    
    {"Query": "What is considered an accessory to my car?",
     "Response": "Accessories are parts or products specifically designed to be fitted to your car, including electric car charging cables and the home charger."},
    
    {"Query": "What should I do if my car needs to be stored safely after an accident?",
     "Response": "We will cover the reasonable cost of storing your car if it needs to be stored safely at any time."},
    
    {"Query": "What are the territorial limits of the policy?",
     "Response": "The territorial limits include Great Britain, Northern Ireland, the Channel Islands, and the Isle of Man."},
    
    {"Query": "How is the policy booklet structured?", 
     "Response": "The policy booklet includes sections such as FAQs, Glossary, Making a Claim, detailed coverage sections, additional services and conditions, complaints, and contacts."},
    
    {"Query": "What is considered vandalism?",
     "Response": "Vandalism is damage caused by a malicious and deliberate act."},
    
    {"Query": "Can I use my car for track days?", 
     "Response": "No, track days, where your car is driven on a racing track, airfield, or off-road event, are not covered."},
    
    {"Query": "How do I pay an excess for a claim?", 
     "Response": "You will need to pay the excess for some claims, which is detailed in your car insurance details."},
    
    {"Query": "Are convertible cars covered under the policy?", 
     "Response": "Yes, convertibles, also known as cabriolets, roadsters, soft-tops, or hard-tops, are covered under the policy."},
    
    {"Query": "What is the process for windscreen repairs?", 
     "Response": "If you arrange windscreen repairs with someone who isn’t an approved supplier, you don’t need approval beforehand, but coverage is limited."},
    
    {"Query": "What is an approved repairer?", 
     "Response": "An approved repairer is a repairer in our network who is authorized to carry out repairs to your car following a claim."},
    
    {"Query": "How can I contact Churchill if I have a complaint?",
     "Response": "Details on how to make a complaint are provided in the 'If you have a complaint' section on page 42."}
]

df = pd.DataFrame(data)
df.to_csv("dataset.csv", index=False)
