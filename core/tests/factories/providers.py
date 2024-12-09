from faker import Faker
from faker.providers import DynamicProvider

faker = Faker()

generate_order_item_provider = DynamicProvider(
    provider_name="order_item",
    elements=[
        ("Blueberry Mint", "FLAVOUR"),
        ("Double Apple", "FLAVOUR"),
        ("Peach", "FLAVOUR"),
        ("Head", "EXTRA"),
        ("Ice Pipe", "EXTRA"),
    ],
)

faker.add_provider(generate_order_item_provider)
