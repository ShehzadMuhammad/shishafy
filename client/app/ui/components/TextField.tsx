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
      <div className="w-full max-w-sm min-w-[200px]">
        <input
          type="text"
          name={name}
          className="w-full bg-white-100 placeholder:text-slate-400 text-slate-700 text-sm border border-slate-200 rounded-md px-3 py-2 transition duration-300 ease focus:outline-none focus:border-slate-400 hover:border-slate-300 shadow-sm focus:shadow"
          placeholder={placeholder}
        />
      </div>
    </Column>
  );
};
