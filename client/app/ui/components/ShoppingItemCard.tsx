import { Button } from "./Button";
import { Column } from "./Column";
import { Row } from "./Row";

interface Props {
  label: string;
  image: string;
  price: string;
  description: string;
  onIncrease: () => void;
  onDecrease: () => void;
}

export const ShoppingItemCard: React.FC<Props> = ({
  label,
  image,
  price,
  description,
  onIncrease,
  onDecrease,
}) => {
  return (
    <Column
      gap="gap-2"
      className="w-60 justify-center p-6 bg-white rounded-xl shadow-lg"
    >
      <span>{label}</span>
      <span>{image}</span>
      <span>{description}</span>
      <span>${price}</span>
      <Row gap="gap-2" className="justify-center">
        <Button sm onClick={onDecrease} label="-" />
        <Button sm onClick={onIncrease} label="+" />
      </Row>
    </Column>
  );
};
