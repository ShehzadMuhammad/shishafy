interface Props {
  children: React.ReactNode;
  gap?: "gap-2" | "gap-4" | "gap-6";
  center?: boolean;
  spaceBetween?: boolean;
  justifyStart?: boolean;
  justifyEnd?: boolean;
}

export const Row: React.FC<Props> = ({
  children,
  gap,
  center,
  spaceBetween,
  justifyStart,
  justifyEnd,
}) => {
  return (
    <div
      className={`flex flex-row flex-wrap ${gap} ${
        center && "justify-center"
      } ${spaceBetween && "justify-between"}
      ${justifyStart && "justify-start"}
      ${justifyEnd && "justify-end"}
      `}
    >
      {children}
    </div>
  );
};
