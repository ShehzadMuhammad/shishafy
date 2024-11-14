"use client";

import { Button } from "@/app/ui/components/Button";
import { Column } from "@/app/ui/components/Column";
import { NavBar } from "@/app/ui/components/Navbar";
import { Row } from "@/app/ui/components/Row";
import { Section } from "@/app/ui/components/Section";
import { ItemSelectionStep } from "@/app/ui/order/ItemSelectionStep";
import { PersonalInfoStep } from "@/app/ui/order/PersonalInfoStep";
import { useState } from "react";

export default function Page() {
  const [orderStep, setOrderStep] = useState(0);
  const [shoppingCart, setShoppingCart] = useState([]);

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

      <Section rounded backgroundColour="bg-slate-300">
        <Column gap="gap-4">
          {orderStep === 0 && <ItemSelectionStep />}
          {orderStep === 1 && <PersonalInfoStep />}
          <Row gap="gap-2" justifyEnd>
            <Button
              md
              label="Previous"
              onClick={() => setOrderStep(orderStep - 1)}
              hidden={orderStep == 0}
            />
            <Button
              md
              label="Next"
              onClick={() => setOrderStep(orderStep + 1)}
              hidden={orderStep == 2}
            />
          </Row>
        </Column>
      </Section>
    </Column>
  );
}
