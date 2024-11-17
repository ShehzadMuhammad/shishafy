import { Column } from "@/app/ui/components/Column";
import { NavBar } from "@/app/ui/components/Navbar";
import { Section } from "@/app/ui/components/Section";
import { OrderPageContents } from "@/app/ui/order/OrderPageContents";

export default function Page() {
  return (
    <Column gap="gap-2">
      <Section>
        <NavBar />
        <div className="mt-28 mb-15">
          <Column gap="gap-2">
            <span className="text-7xl">Start Your Experience.</span>
            <p>
              Choose from our selection of shisha flavours, we will make a
              confirmation call to confirm your order.
            </p>
          </Column>
        </div>
      </Section>
      <OrderPageContents />
    </Column>
  );
}
