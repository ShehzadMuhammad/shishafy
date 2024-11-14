import { Column } from "@/app/ui/components/Column";
import { Row } from "@/app/ui/components/Row";
import { ShoppingItemCard } from "@/app/ui/components/ShoppingItemCard";

export const ItemSelectionStep: React.FC = () => {
  return (
    <Column gap="gap-2">
      <span className="text-lg">Please Select Your Shisha Flavour.</span>
      <Row gap="gap-2">
        <ShoppingItemCard
          onDecrease={() => console.log("Decreased Flavour")}
          onIncrease={() => console.log("Clicked")}
          label="Blueberry Mist"
          image="image"
          price="19.29"
        />
        <ShoppingItemCard
          onDecrease={() => console.log("Decreased Flavour")}
          onIncrease={() => console.log("Clicked")}
          label="Blueberry Mist"
          image="image"
          price="19.29"
        />
        <ShoppingItemCard
          onDecrease={() => console.log("Decreased Flavour")}
          onIncrease={() => console.log("Clicked")}
          label="Blueberry Mist"
          image="image"
          price="19.29"
        />
        <ShoppingItemCard
          onDecrease={() => console.log("Decreased Flavour")}
          onIncrease={() => console.log("Clicked")}
          label="Blueberry Mist"
          image="image"
          price="19.29"
        />
      </Row>
      <span className="text-lg">Extras</span>
      <Row gap="gap-2">
        <ShoppingItemCard
          onDecrease={() => console.log("Decreased Extra")}
          onIncrease={() => console.log("extra")}
          label="Head"
          image="image"
          price="5.00"
        />
      </Row>
    </Column>
  );
};
