"use client";

import { Button } from "@/app/ui/components/Button";
import { Row } from "@/app/ui/components/Row";
import { Section } from "@/app/ui/components/Section";
import { ItemSelectionStep } from "@/app/ui/order/ItemSelectionStep";
import { PersonalInfoStep } from "@/app/ui/order/PersonalInfoStep";
import { useState } from "react";

export const OrderPageContents: React.FC = () => {
  const [orderStep, setOrderStep] = useState(0);

  return (
    <Section isRounded className="bg-slate-300 gap-3">
      {orderStep === 0 && <ItemSelectionStep />}
      {orderStep === 1 && <PersonalInfoStep />}
      <Row gap="gap-2" className="justify-end mt-auto">
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
    </Section>
  );
};
