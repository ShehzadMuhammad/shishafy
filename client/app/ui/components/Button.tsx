import clsx from "clsx";

interface Props {
  onClick: () => void;
  label: string;
  sm?: boolean;
  md?: boolean;
  hidden?: boolean;
}

export const Button: React.FC<Props> = ({ onClick, label, sm, md, hidden }) => {
  if (hidden) return null;

  return (
    <button
      className={clsx(
        "text-white",
        "font-bold",
        "hover:bg-slate-800",
        "cursor-pointer",
        sm && "px-2",
        md && "p-3",
        "bg-sky-500",
        "rounded-xl",
        "shadow-lg"
      )}
      onClick={onClick}
    >
      {label}
    </button>
  );
};
