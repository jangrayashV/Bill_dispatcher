# coupons mapped to discount value in a dict
coupons = {"get25": 25,"save40": 40,"off50": 50}

user_amount_input = int(input("Enter your  amount : "))
coupon_applied = input("Enter your coupon code: ").lower().replace(" ", "")

def bill_dispatcher(amount, coupon):
    # using dispatch table pattern
    discount = coupons.get(coupon_applied, 0)

    if discount!=0 :
        print("valid coupon code, discount applied :)") 
    else:
        print("invalid coupon code, no discount applied :(")

    discount_amount = amount - amount * (discount / 100)
    print(f"Your final amount after applying \"{coupon}\" is : {discount_amount}")

bill_dispatcher(user_amount_input, coupon_applied)