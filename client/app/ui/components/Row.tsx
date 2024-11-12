interface Props {
  children: React.ReactNode;
  gap?: "gap-2" | "gap-4" | "gap-6";
  center?: boolean;
}

export const Row: React.FC<Props> = ({ children, gap, center }) => {
  return (
    <div
      className={`flex flex-row flex-wrap ${gap} ${center && "justify-center"}`}
    >
      {children}
    </div>
  );
};
