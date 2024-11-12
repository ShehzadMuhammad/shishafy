import { Column } from "./Column";
import Image from "next/image";

interface Props {
  title: string;
  description: string;
  imageSrc: string;
  imageAlt: string;
}

export const InfoCard: React.FC<Props> = ({
  title,
  description,
  imageSrc,
  imageAlt,
}) => {
  return (
    <div className="flex flex-col w-56 justify-center p-6 max-w-sm mx-auto bg-white rounded-xl shadow-lg">
      <Column gap="gap-4">
        <p className="text-center font-bold">{title}</p>
        <Image className="mx-auto" src={imageSrc} width={100} alt={imageAlt} />
        <p>{description} </p>
      </Column>
    </div>
  );
};
