import { NavBar } from "@/app/ui/components/Navbar";
import { Section } from "@/app/ui/components/Section";
import { Column } from "../ui/components/Column";
import { TextField } from "../ui/components/TextField";

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
          <TextField name="name" placeholder="Enter Your Name" />
          <label>Email</label>
          <TextField name="email" placeholder="Enter Your Email" />
          <label>Phone Number</label>
          <input
            type="tel"
            name="phone"
            className="block w-full rounded-md border-0 py-1.5 pl-7 pr-20 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm/6"
            placeholder="Enter Your Phone Number"
          />
          <label>Address</label>
          <TextField name="address" placeholder="Enter Your Address" />
          <label>Flavour</label>
          <select
            id="flavour"
            className="block w-full rounded-md border-0 py-1.5 pl-7 pr-20 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm/6"
          >
            <option selected>Choose a flavour(s)</option>
            <option value="Blueberry">Blueberry</option>
            <option value="Double-Apple">Double Apple</option>
            <option value="Watermelon">Watermelon</option>
            <option value="Peach-Herbal">Peach - Herbal</option>
          </select>
        </Column>
        <Column>
          <p>Order</p>
        </Column>
      </Section>
    </>
  );
}
