# stripe sample to create product and price
import stripe
stripe.api_key = 'sk_test_51NO3L7CPqr0REwvSdGB4OC7J074gQy0DibiWnTuta3MiMroU9PDybfGNwU4MTrnS1aLpDX5DgvRG8thAvNXuQs2000p5xiCZal'

air_conditioner = stripe.Product.create(
    name='Air Conditioner',
    type='good',
    description='A used good quality air conditioner',
    attributes=['size', 'color'],
)

air_conditioner_price = stripe.Price.create(
    # the price is in cents 100cents = 1euro
    unit_amount=10000,
    currency='eur',
    product=air_conditioner.id,
)

print(f'Air Conditioner Product ID: {air_conditioner.id}')
print(f'Air Conditioner Price ID: {air_conditioner_price.id}')


starter_subscription = stripe.Product.create(
    name='Starter Subscription',
    type='service',
    description='€5/Month subscription',
)

starter_subscription_price = stripe.Price.create(
    unit_amount=1500,
    currency='eur',
    recurring={"interval": "month"},
    product=starter_subscription.id,
)

print(f'Starter Subscription Product ID: {starter_subscription.id}')
print(f'Starter Subscription Price ID: {starter_subscription_price.id}')