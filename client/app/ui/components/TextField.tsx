import { Column } from "./Column";

interface Props {
  name: string;
  label: string;
  placeholder: string;
}

export const TextField: React.FC<Props> = ({ label, name, placeholder }) => {
  return (
    <Column gap="gap-1">
      <label>{label}</label>
      <input
        type="text"
        name={name}
        className="block w-full rounded-md border-0 py-1.5 pl-7 pr-20 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm/6"
        placeholder={placeholder}
      />
    </Column>
  );
};
