import rstr
from faker import Faker
from faker.providers import DynamicProvider

faker = Faker("en_CA")

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

generate_postal_code_provider = DynamicProvider(
    provider_name="postal_code",
    elements=[rstr.xeger(r"[A-Z]\d[A-Z] \d[A-Z]\d") for _ in range(100)],
)

faker.add_provider(generate_order_item_provider)
faker.add_provider(generate_postal_code_provider)
