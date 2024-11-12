import { Button } from "./Button";
import { Row } from "./Row";

interface Props {
  label: string;
  image: string;
  price: string;
  onClick: () => void;
}

export const ShoppingItemCard: React.FC<Props> = ({
  label,
  image,
  price,
  onClick,
}) => {
  return (
    <div className="flex flex-col w-56 justify-center p-6 bg-white rounded-xl shadow-lg">
      <span>{label}</span>
      <span>{image}</span>
      <span>${price}</span>
      <Row gap="gap-2" center>
        <Button onClick={onClick} label="-" />
        <Button onClick={onClick} label="+" />
      </Row>
    </div>
  );
};
