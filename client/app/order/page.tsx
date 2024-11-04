import { NavBar } from "@/app/ui/components/Navbar";
import { Section } from "@/app/ui/components/Section";
import { Column } from "../ui/components/Column";

export default function Page() {
  return (
    <>
      <Section rounded backgroundColour="bg-fuchsia-400">
        <NavBar />
        <div className="mt-28 mb-20">
          <Column gap="gap-2">
            <p className="text-7xl">Start Your Experience.</p>
            <p>
              Choose from our selection of shisha flavours, we will make a
              confirmation call to confirm your order.
            </p>
          </Column>
        </div>
      </Section>
      <Section>
        <Column>
          <label>Name</label>
          <input
            type="text"
            name="name"
            className="block w-full rounded-md border-0 py-1.5 pl-7 pr-20 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm/6"
            placeholder="Enter Your Name"
          />
          <p>Email</p>
          <p>Number</p>
          <p>address</p>
          <p>Quantity</p>
          <p>Extra(s)</p>
          <p>Flavour</p>
        </Column>
        <Column>
          <p>Order</p>
        </Column>
      </Section>
    </>
  );
}
