import { Column } from "@/app/ui/components/Column";
import { Row } from "@/app/ui/components/Row";
import { ShoppingItemCard } from "@/app/ui/components/ShoppingItemCard";

export const ItemSelectionStep: React.FC = () => {
  return (
    <Column gap="gap-2">
      <span className="text-lg">Please Select Your Shisha Flavour.</span>
      <Row gap="gap-4" className="flex-wrap">
        <ShoppingItemCard
          onDecrease={() => console.log("Decreased Flavour")}
          onIncrease={() => console.log("Clicked")}
          label="Blueberry Mist"
          image="image"
          price="19.29"
          description="Blueberry mixed with Mint"
        />
        <ShoppingItemCard
          onDecrease={() => console.log("Decreased Flavour")}
          onIncrease={() => console.log("Clicked")}
          label="Double Apple"
          image="image"
          price="19.29"
          description="The traditional shisha flavour, gives off an apple taste that is consider more harsh."
        />
        <ShoppingItemCard
          onDecrease={() => console.log("Decreased Flavour")}
          onIncrease={() => console.log("Clicked")}
          label="Watermelon"
          image="image"
          price="19.29"
          description="Watermelon mixed with mint."
        />
        <ShoppingItemCard
          onDecrease={() => console.log("Decreased Flavour")}
          onIncrease={() => console.log("Clicked")}
          label="Peach"
          image="image"
          description="Fruity peach"
          price="19.29"
        />
      </Row>
      <span className="text-lg">Extras</span>
      <Row gap="gap-4" className="flex-wrap">
        <ShoppingItemCard
          onDecrease={() => console.log("Decreased Extra")}
          onIncrease={() => console.log("extra")}
          label="Head"
          image="image"
          description="Add an extra head for the same flavour to extend your hookah session."
          price="5.00"
        />
      </Row>
    </Column>
  );
};
