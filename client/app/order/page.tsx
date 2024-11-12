"use client";

import { NavBar } from "@/app/ui/components/Navbar";
import { Section } from "@/app/ui/components/Section";
import { Column } from "@/app/ui/components/Column";
import { ShoppingItemCard } from "../ui/components/ShoppingItemCard";
import { Box } from "../ui/components/Box";
import { Row } from "../ui/components/Row";

export default function Page() {
  return (
    <Column gap="gap-2">
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
      <Section rounded backgroundColour="bg-slate-300">
        <Column gap="gap-2">
          <span>Please Select Your Shisha Flavour.</span>
          <Row gap="gap-2">
            <ShoppingItemCard
              onClick={() => console.log("Clicked")}
              label="Blueberry Mist"
              image="image"
              price="19.29"
            />
            <ShoppingItemCard
              onClick={() => console.log("Clicked")}
              label="Blueberry Mist"
              image="image"
              price="19.29"
            />
            <ShoppingItemCard
              onClick={() => console.log("Clicked")}
              label="Blueberry Mist"
              image="image"
              price="19.29"
            />
            <ShoppingItemCard
              onClick={() => console.log("Clicked")}
              label="Blueberry Mist"
              image="image"
              price="19.29"
            />
          </Row>
        </Column>
      </Section>
    </Column>
  );
}
