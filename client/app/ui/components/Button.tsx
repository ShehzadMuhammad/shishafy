interface Props {
  onClick: () => void;
  label: string;
}

export const Button: React.FC<Props> = ({ onClick, label }) => {
  return (
    <button
      className="text-white font-bold hover:bg-slate-800 w-6  bg-slate-400 rounded-xl shadow-lg"
      onClick={onClick}
    >
      {label}
    </button>
  );
};
