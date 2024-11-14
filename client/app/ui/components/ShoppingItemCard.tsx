import { Button } from "./Button";
import { Row } from "./Row";

interface Props {
  label: string;
  image: string;
  price: string;
  onIncrease: () => void;
  onDecrease: () => void;
}

export const ShoppingItemCard: React.FC<Props> = ({
  label,
  image,
  price,
  onIncrease,
  onDecrease,
}) => {
  return (
    <div className="flex flex-col w-56 justify-center p-6 bg-white rounded-xl shadow-lg">
      <span>{label}</span>
      <span>{image}</span>
      <span>${price}</span>
      <Row gap="gap-2" center>
        <Button sm onClick={onDecrease} label="-" />
        <Button sm onClick={onIncrease} label="+" />
      </Row>
    </div>
  );
};
