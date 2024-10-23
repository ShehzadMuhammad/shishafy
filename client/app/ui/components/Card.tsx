import { Column } from "./Column";

interface Props {
  title: string;
  description: string;
  image: string;
}

export const Card: React.FC<Props> = ({ title, description, image }) => {
  return (
    <div className="p-2 max-w-sm bg-pink-300 rounded-xl shadow-2xl">
      <Column gap="gap-4">
        <p className="text-center">{title}</p>
        <p>{image}</p>
        <p>{description} </p>
      </Column>
    </div>
  );
};
